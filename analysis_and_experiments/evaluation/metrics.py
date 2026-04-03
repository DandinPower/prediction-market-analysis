from typing import Any, Sequence

import numpy as np
import torch
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    log_loss,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)

from analysis_and_experiments.strategies.common import BinaryMetrics


def _to_numpy_1d(tensor: torch.Tensor) -> np.ndarray:
    return tensor.detach().cpu().squeeze(1).numpy()


def evaluate_binary_metrics(
    y_true_tensor: torch.Tensor,
    y_prob: Sequence[float] | np.ndarray,
    *,
    classification_threshold: float = 0.5,
) -> BinaryMetrics:
    y_true = _to_numpy_1d(y_true_tensor)
    y_prob_np = np.asarray(list(y_prob), dtype=np.float64)
    y_prob_clipped = np.clip(y_prob_np, 1e-9, 1.0 - 1e-9)
    y_pred = (y_prob_np >= classification_threshold).astype(int)

    sklearn_loss = float(log_loss(y_true, y_prob_clipped, labels=[0, 1]))
    torch_loss = float(
        torch.nn.BCELoss()(
            torch.tensor(y_prob_clipped, dtype=torch.float32).unsqueeze(1),
            y_true_tensor.float(),
        ).item()
    )

    accuracy = float(accuracy_score(y_true, y_pred))
    precision = float(precision_score(y_true, y_pred, zero_division=0))
    recall = float(recall_score(y_true, y_pred, zero_division=0))
    f1 = float(f1_score(y_true, y_pred, zero_division=0))

    auc: float | None
    roc_fpr: list[float] | None
    roc_tpr: list[float] | None
    if len(set(y_true.tolist())) < 2:
        auc = None
        roc_fpr = None
        roc_tpr = None
    else:
        auc = float(roc_auc_score(y_true, y_prob_np))
        fpr, tpr, _ = roc_curve(y_true, y_prob_np)
        roc_fpr = [float(value) for value in fpr]
        roc_tpr = [float(value) for value in tpr]

    return BinaryMetrics(
        sklearn_log_loss=sklearn_loss,
        torch_bce_loss=torch_loss,
        accuracy=accuracy,
        precision=precision,
        recall=recall,
        f1=f1,
        auc=auc,
        roc_fpr=roc_fpr,
        roc_tpr=roc_tpr,
    )


def to_numpy_1d(tensor: torch.Tensor) -> Any:
    """Compatibility helper for legacy wrappers."""
    return _to_numpy_1d(tensor)
