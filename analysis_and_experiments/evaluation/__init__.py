"""Model evaluation utilities."""

from .margin import calculate_average_margin_of_victory
from .metrics import evaluate_binary_metrics

__all__ = ["calculate_average_margin_of_victory", "evaluate_binary_metrics"]
