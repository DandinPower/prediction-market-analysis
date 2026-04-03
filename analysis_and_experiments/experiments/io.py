import csv
import json
from pathlib import Path
from typing import Any

from analysis_and_experiments.strategies.common import ExperimentSummary, FoldResult, RunResult


def _run_to_flat_row(run: RunResult) -> dict[str, Any]:
    return {
        "preset": run.preset,
        "strategy": run.strategy,
        "truncate_and_keep_ratio": run.truncate_and_keep_ratio,
        "desired_num_candlesticks": run.desired_num_candlesticks,
        "cv_enabled": run.cv_enabled,
        "cv_folds": run.cv_folds,
        "train_log_loss": run.train_metrics.sklearn_log_loss,
        "train_bce_loss": run.train_metrics.torch_bce_loss,
        "train_accuracy": run.train_metrics.accuracy,
        "train_precision": run.train_metrics.precision,
        "train_recall": run.train_metrics.recall,
        "train_f1": run.train_metrics.f1,
        "train_auc": run.train_metrics.auc,
        "val_log_loss": run.val_metrics.sklearn_log_loss,
        "val_bce_loss": run.val_metrics.torch_bce_loss,
        "val_accuracy": run.val_metrics.accuracy,
        "val_precision": run.val_metrics.precision,
        "val_recall": run.val_metrics.recall,
        "val_f1": run.val_metrics.f1,
        "val_auc": run.val_metrics.auc,
        "average_margin_of_victory": run.average_margin_of_victory,
        "roc_plot_path": str(run.roc_plot_path) if run.roc_plot_path is not None else None,
        "gru_train_curve_plot_path": (
            str(run.gru_train_curve_plot_path) if run.gru_train_curve_plot_path is not None else None
        ),
        "gru_val_curve_plot_path": (
            str(run.gru_val_curve_plot_path) if run.gru_val_curve_plot_path is not None else None
        ),
        "train_confusion_matrix_plot_path": (
            str(run.train_confusion_matrix_plot_path)
            if run.train_confusion_matrix_plot_path is not None
            else None
        ),
        "val_confusion_matrix_plot_path": (
            str(run.val_confusion_matrix_plot_path) if run.val_confusion_matrix_plot_path is not None else None
        ),
    }


def _fold_to_flat_row(run: RunResult, fold: FoldResult) -> dict[str, Any]:
    return {
        "preset": run.preset,
        "strategy": run.strategy,
        "truncate_and_keep_ratio": run.truncate_and_keep_ratio,
        "desired_num_candlesticks": run.desired_num_candlesticks,
        "cv_enabled": run.cv_enabled,
        "cv_folds": run.cv_folds,
        "fold_index": fold.fold_index,
        "train_size": fold.train_size,
        "val_size": fold.val_size,
        "train_log_loss": fold.train_metrics.sklearn_log_loss,
        "train_bce_loss": fold.train_metrics.torch_bce_loss,
        "train_accuracy": fold.train_metrics.accuracy,
        "train_precision": fold.train_metrics.precision,
        "train_recall": fold.train_metrics.recall,
        "train_f1": fold.train_metrics.f1,
        "train_auc": fold.train_metrics.auc,
        "val_log_loss": fold.val_metrics.sklearn_log_loss,
        "val_bce_loss": fold.val_metrics.torch_bce_loss,
        "val_accuracy": fold.val_metrics.accuracy,
        "val_precision": fold.val_metrics.precision,
        "val_recall": fold.val_metrics.recall,
        "val_f1": fold.val_metrics.f1,
        "val_auc": fold.val_metrics.auc,
        "average_margin_of_victory": fold.average_margin_of_victory,
    }


def write_summary_outputs(
    summary: ExperimentSummary,
    output_root: Path,
) -> tuple[Path, Path, Path]:
    result_dir = output_root / "results" / summary.preset
    result_dir.mkdir(parents=True, exist_ok=True)

    csv_path = result_dir / "summary.csv"
    folds_csv_path = result_dir / "summary_folds.csv"
    json_path = result_dir / "summary.json"

    rows = [_run_to_flat_row(run) for run in summary.runs]
    fold_rows = [
        _fold_to_flat_row(run, fold)
        for run in summary.runs
        for fold in run.fold_results
    ]

    if rows:
        with open(csv_path, "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    else:
        with open(csv_path, "w", encoding="utf-8") as csvfile:
            csvfile.write("\n")

    if fold_rows:
        with open(folds_csv_path, "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(fold_rows[0].keys()))
            writer.writeheader()
            writer.writerows(fold_rows)
    else:
        with open(folds_csv_path, "w", encoding="utf-8") as csvfile:
            csvfile.write("\n")

    payload = {
        "preset": summary.preset,
        "runs": [run.to_dict() for run in summary.runs],
        "ranking_by_margin": summary.ranking_by_margin,
        "ranking_by_auc": summary.ranking_by_auc,
    }

    with open(json_path, "w", encoding="utf-8") as jsonfile:
        json.dump(payload, jsonfile, indent=2)

    return csv_path, folds_csv_path, json_path
