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
class RunResult:
    preset: str
    strategy: str
    truncate_and_keep_ratio: float
    desired_num_candlesticks: int | None
    train_metrics: BinaryMetrics
    val_metrics: BinaryMetrics
    average_margin_of_victory: float
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
        return payload


@dataclass
class ExperimentSummary:
    preset: str
    runs: list[RunResult]
    ranking_by_margin: list[dict[str, Any]]
    ranking_by_auc: list[dict[str, Any]]
