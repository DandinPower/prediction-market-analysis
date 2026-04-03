from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass
class BinaryMetrics:
    sklearn_log_loss: float
    torch_bce_loss: float
    accuracy: float
    precision: float
    recall: float
    f1: float
    auc: float | None
    roc_fpr: list[float] | None
    roc_tpr: list[float] | None


@dataclass
class FoldResult:
    fold_index: int
    train_size: int
    val_size: int
    train_metrics: BinaryMetrics
    val_metrics: BinaryMetrics
    average_margin_of_victory: float

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class RunResult:
    preset: str
    strategy: str
    truncate_and_keep_ratio: float
    desired_num_candlesticks: int | None
    cv_enabled: bool
    cv_folds: int | None
    train_metrics: BinaryMetrics
    val_metrics: BinaryMetrics
    average_margin_of_victory: float
    fold_results: list[FoldResult]
    roc_plot_path: Path | None
    gru_train_curve_plot_path: Path | None = None
    gru_val_curve_plot_path: Path | None = None
    train_confusion_matrix_plot_path: Path | None = None
    val_confusion_matrix_plot_path: Path | None = None

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["roc_plot_path"] = str(self.roc_plot_path) if self.roc_plot_path is not None else None
        payload["gru_train_curve_plot_path"] = (
            str(self.gru_train_curve_plot_path)
            if self.gru_train_curve_plot_path is not None
            else None
        )
        payload["gru_val_curve_plot_path"] = (
            str(self.gru_val_curve_plot_path) if self.gru_val_curve_plot_path is not None else None
        )
        payload["train_confusion_matrix_plot_path"] = (
            str(self.train_confusion_matrix_plot_path)
            if self.train_confusion_matrix_plot_path is not None
            else None
        )
        payload["val_confusion_matrix_plot_path"] = (
            str(self.val_confusion_matrix_plot_path)
            if self.val_confusion_matrix_plot_path is not None
            else None
        )
        payload["fold_results"] = [fold.to_dict() for fold in self.fold_results]
        return payload


@dataclass
class ExperimentSummary:
    preset: str
    runs: list[RunResult]
    ranking_by_margin: list[dict[str, Any]]
    ranking_by_auc: list[dict[str, Any]]


def average_binary_metrics(metrics: list[BinaryMetrics]) -> BinaryMetrics:
    if not metrics:
        raise ValueError("metrics cannot be empty.")

    auc_values = [metric.auc for metric in metrics if metric.auc is not None]

    return BinaryMetrics(
        sklearn_log_loss=float(sum(metric.sklearn_log_loss for metric in metrics) / len(metrics)),
        torch_bce_loss=float(sum(metric.torch_bce_loss for metric in metrics) / len(metrics)),
        accuracy=float(sum(metric.accuracy for metric in metrics) / len(metrics)),
        precision=float(sum(metric.precision for metric in metrics) / len(metrics)),
        recall=float(sum(metric.recall for metric in metrics) / len(metrics)),
        f1=float(sum(metric.f1 for metric in metrics) / len(metrics)),
        auc=float(sum(auc_values) / len(auc_values)) if auc_values else None,
        roc_fpr=None,
        roc_tpr=None,
    )
