from typing import Sequence


def calculate_average_margin_of_victory(
    probabilities: Sequence[float],
    reference_prices: Sequence[float],
) -> float:
    """Calculate average expected margin using model probability and reference entry price."""
    if len(probabilities) != len(reference_prices):
        raise ValueError("probabilities and reference_prices must have the same length.")
    if not probabilities:
        raise ValueError("probabilities cannot be empty.")

    margin_of_victory = 0.0
    for probability, price in zip(probabilities, reference_prices, strict=True):
        winning_margin = 1.0 - float(price)
        expected_margin = float(probability) * winning_margin
        expected_loss = (1.0 - float(probability)) * float(price)
        margin_of_victory += expected_margin - expected_loss

    return float(margin_of_victory / len(reference_prices))
