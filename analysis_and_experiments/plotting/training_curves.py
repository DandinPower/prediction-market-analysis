import os
from pathlib import Path
from typing import Sequence

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def save_train_val_metric_plot(
    *,
    output_path: Path,
    title: str,
    metric_name: str,
    train_values: Sequence[float],
    val_values: Sequence[float],
    y_limit: tuple[float, float] | None = None,
    dpi: int = 300,
) -> Path:
    if len(train_values) != len(val_values):
        raise ValueError("train_values and val_values must have the same length.")
    if not train_values:
        raise ValueError("train_values cannot be empty.")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    epochs = list(range(1, len(train_values) + 1))
    fig, axis = plt.subplots(figsize=(8, 5))
    axis.plot(
        epochs,
        list(train_values),
        color="#1f77b4",
        linewidth=2,
        label=f"Train {metric_name}",
    )
    axis.plot(
        epochs,
        list(val_values),
        color="#ff7f0e",
        linewidth=2,
        label=f"Val {metric_name}",
    )

    axis.set_xlabel("Epoch")
    axis.set_ylabel(metric_name)
    axis.set_title(title)
    if y_limit is not None:
        axis.set_ylim(*y_limit)
    axis.legend(loc="best")

    fig.tight_layout()
    fig.savefig(output_path, dpi=dpi)
    plt.close(fig)
    return output_path
