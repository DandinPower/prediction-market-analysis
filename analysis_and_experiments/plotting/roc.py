import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def save_roc_plot(
    *,
    output_path: Path,
    title: str,
    roc_fpr: list[float] | None,
    roc_tpr: list[float] | None,
    auc: float | None,
    dpi: int = 300,
) -> Path | None:
    if roc_fpr is None or roc_tpr is None or auc is None:
        return None

    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(7, 5))
    plt.plot(roc_fpr, roc_tpr, label=f"AUC={auc:.4f}", linewidth=2)
    plt.plot([0.0, 1.0], [0.0, 1.0], linestyle="--", linewidth=1)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(title)
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(output_path, dpi=dpi)
    plt.close()
    return output_path
