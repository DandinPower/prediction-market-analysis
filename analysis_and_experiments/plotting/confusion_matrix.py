import os
from pathlib import Path
from typing import Sequence

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix


def save_confusion_matrix_plot(
    *,
    output_path: Path,
    title: str,
    y_true: Sequence[int],
    y_pred: Sequence[int],
    class_names: tuple[str, str] = ("No", "Yes"),
    dpi: int = 300,
) -> Path:
    matrix = confusion_matrix(y_true, y_pred, labels=[0, 1])

    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(6, 5))
    image = ax.imshow(matrix, cmap="Blues")
    fig.colorbar(image, ax=ax)

    ticks = np.arange(len(class_names))
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(class_names)
    ax.set_yticklabels(class_names)
    ax.set_xlabel("Predicted Label")
    ax.set_ylabel("True Label")
    ax.set_title(title)

    threshold = matrix.max() / 2.0 if matrix.size else 0.0
    for row_index in range(matrix.shape[0]):
        for col_index in range(matrix.shape[1]):
            value = int(matrix[row_index, col_index])
            text_color = "white" if matrix[row_index, col_index] > threshold else "black"
            ax.text(
                col_index,
                row_index,
                f"{value}",
                ha="center",
                va="center",
                color=text_color,
            )

    fig.tight_layout()
    fig.savefig(output_path, dpi=dpi)
    plt.close(fig)
    return output_path
