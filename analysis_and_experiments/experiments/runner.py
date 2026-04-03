import argparse
from pathlib import Path
from typing import Any, Callable

from analysis_and_experiments.data import btc_market_filter_policy, market_filter_policy
from analysis_and_experiments.experiments.io import write_summary_outputs
from analysis_and_experiments.experiments.presets import PRESET_ORDER, build_preset_tasks
from analysis_and_experiments.strategies import (
    ExperimentSummary,
    RunResult,
    run_gru_experiment_on_ratio,
    run_tabular_experiment_on_ratio,
)


def _parse_csv_floats(raw: str | None) -> list[float] | None:
    if raw is None:
        return None
    values = [chunk.strip() for chunk in raw.split(",") if chunk.strip()]
    if not values:
        return None
    return [float(value) for value in values]


def _parse_csv_ints(raw: str | None) -> list[int] | None:
    if raw is None:
        return None
    values = [chunk.strip() for chunk in raw.split(",") if chunk.strip()]
    if not values:
        return None
    return [int(value) for value in values]


def _select_market_policy_for_preset(preset: str) -> Callable[[dict[str, Any]], bool]:
    if preset == "exp5":
        return btc_market_filter_policy
    return market_filter_policy


def _build_rankings(runs: list[RunResult]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    ranking_by_margin = []
    for rank, run in enumerate(
        sorted(runs, key=lambda item: item.average_margin_of_victory, reverse=True),
        start=1,
    ):
        ranking_by_margin.append(
            {
                "rank": rank,
                "strategy": run.strategy,
                "truncate_and_keep_ratio": run.truncate_and_keep_ratio,
                "desired_num_candlesticks": run.desired_num_candlesticks,
                "val_auc": run.val_metrics.auc,
                "average_margin_of_victory": run.average_margin_of_victory,
            }
        )

    ranking_by_auc = []
    for rank, run in enumerate(
        sorted(
            runs,
            key=lambda item: item.val_metrics.auc if item.val_metrics.auc is not None else float("-inf"),
            reverse=True,
        ),
        start=1,
    ):
        ranking_by_auc.append(
            {
                "rank": rank,
                "strategy": run.strategy,
                "truncate_and_keep_ratio": run.truncate_and_keep_ratio,
                "desired_num_candlesticks": run.desired_num_candlesticks,
                "val_auc": run.val_metrics.auc,
                "average_margin_of_victory": run.average_margin_of_victory,
            }
        )

    return ranking_by_margin, ranking_by_auc


def _print_run_result(run: RunResult) -> None:
    train_auc_text = f"{run.train_metrics.auc:.4f}" if run.train_metrics.auc is not None else "N/A"
    val_auc_text = f"{run.val_metrics.auc:.4f}" if run.val_metrics.auc is not None else "N/A"
    print(
        f"[{run.preset}] strategy={run.strategy}, ratio={run.truncate_and_keep_ratio:.2f}, "
        f"candles={run.desired_num_candlesticks}"
    )
    print(
        "Train | "
        f"log_loss={run.train_metrics.sklearn_log_loss:.6f}, "
        f"bce_loss={run.train_metrics.torch_bce_loss:.6f}, "
        f"acc={run.train_metrics.accuracy:.4f}, "
        f"precision={run.train_metrics.precision:.4f}, "
        f"recall={run.train_metrics.recall:.4f}, "
        f"f1={run.train_metrics.f1:.4f}, "
        f"auc={train_auc_text}"
    )
    print(
        "Val   | "
        f"log_loss={run.val_metrics.sklearn_log_loss:.6f}, "
        f"bce_loss={run.val_metrics.torch_bce_loss:.6f}, "
        f"acc={run.val_metrics.accuracy:.4f}, "
        f"precision={run.val_metrics.precision:.4f}, "
        f"recall={run.val_metrics.recall:.4f}, "
        f"f1={run.val_metrics.f1:.4f}, "
        f"auc={val_auc_text}, "
        f"margin={run.average_margin_of_victory:.6f}"
    )
    if run.roc_plot_path is not None:
        print(f"ROC plot saved: {run.roc_plot_path}")
    else:
        print("ROC plot skipped: validation labels contain a single class.")
    if run.gru_train_curve_plot_path is not None:
        print(f"GRU train/val loss plot saved: {run.gru_train_curve_plot_path}")
    if run.gru_val_curve_plot_path is not None:
        print(f"GRU train/val accuracy plot saved: {run.gru_val_curve_plot_path}")
    if run.train_confusion_matrix_plot_path is not None:
        print(f"Train confusion matrix saved: {run.train_confusion_matrix_plot_path}")
    if run.val_confusion_matrix_plot_path is not None:
        print(f"Val confusion matrix saved: {run.val_confusion_matrix_plot_path}")


def run_preset(
    preset: str,
    *,
    mapped_markets_path: Path,
    output_root: Path,
    ratios_override: list[float] | None = None,
    gru_candles_override: list[int] | None = None,
) -> ExperimentSummary:
    tasks = build_preset_tasks(
        preset,
        ratios_override=ratios_override,
        gru_candles_override=gru_candles_override,
    )
    market_policy = _select_market_policy_for_preset(preset)

    print(f"Experiment artifacts are written under: {output_root}")

    runs: list[RunResult] = []
    for task in tasks:
        print(
            f"\nRunning task: preset={task.preset}, strategy={task.strategy}, "
            f"ratio={task.truncate_and_keep_ratio:.2f}, candles={task.desired_num_candlesticks}"
        )

        if task.strategy == "gru":
            result = run_gru_experiment_on_ratio(
                mapped_markets_path,
                task.truncate_and_keep_ratio,
                preset=task.preset,
                desired_num_candlesticks=task.desired_num_candlesticks or 40,
                market_policy=market_policy,
                roc_output_dir=output_root / "plots" / "roc" / "gru",
                train_val_curves_output_dir=output_root / "plots" / "training_curves" / "gru",
                confusion_matrix_output_dir=output_root / "plots" / "confusion_matrix" / "gru",
            )
        elif task.strategy == "tabular":
            result = run_tabular_experiment_on_ratio(
                mapped_markets_path,
                task.truncate_and_keep_ratio,
                preset=task.preset,
                market_policy=market_policy,
                roc_output_dir=output_root / "plots" / "roc" / "tabular",
                confusion_matrix_output_dir=output_root / "plots" / "confusion_matrix" / "tabular",
            )
        else:
            raise ValueError(f"Unsupported strategy: {task.strategy}")

        _print_run_result(result)
        runs.append(result)

    ranking_by_margin, ranking_by_auc = _build_rankings(runs)
    summary = ExperimentSummary(
        preset=preset,
        runs=runs,
        ranking_by_margin=ranking_by_margin,
        ranking_by_auc=ranking_by_auc,
    )

    csv_path, json_path = write_summary_outputs(summary, output_root=output_root)
    print(f"\nSaved summary CSV: {csv_path}")
    print(f"Saved summary JSON: {json_path}")

    return summary


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run modular experiment presets for prediction-market models."
    )
    parser.add_argument(
        "--preset",
        choices=[*PRESET_ORDER, "all"],
        default="all",
        help="Preset to run (default: all).",
    )
    parser.add_argument(
        "--mapped-markets-path",
        type=Path,
        default=Path("datasets/mapped_markets"),
        help="Path to mapped market folder (default: datasets/mapped_markets).",
    )
    parser.add_argument(
        "--ratios",
        type=str,
        default=None,
        help="Optional CSV ratios override, e.g. 0.33,0.67,0.95",
    )
    parser.add_argument(
        "--gru-candles",
        type=str,
        default=None,
        help="Optional CSV GRU candle override, e.g. 40,60,80",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path("outputs"),
        help="Experiment output root (default: outputs).",
    )
    return parser


def main() -> None:
    args = _build_parser().parse_args()
    ratios_override = _parse_csv_floats(args.ratios)
    gru_candles_override = _parse_csv_ints(args.gru_candles)

    if args.preset == "all":
        for preset in PRESET_ORDER:
            print(f"\n================ {preset} ================")
            run_preset(
                preset,
                mapped_markets_path=args.mapped_markets_path,
                output_root=args.output_root,
                ratios_override=ratios_override,
                gru_candles_override=gru_candles_override,
            )
    else:
        run_preset(
            args.preset,
            mapped_markets_path=args.mapped_markets_path,
            output_root=args.output_root,
            ratios_override=ratios_override,
            gru_candles_override=gru_candles_override,
        )


if __name__ == "__main__":
    main()
