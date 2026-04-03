from dataclasses import dataclass

DEFAULT_RATIO_SWEEP = [0.33, 0.50, 0.67, 0.80, 0.95]
DEFAULT_GRU_CANDLES = 40
DEFAULT_EXP4_CANDLE_SWEEP = [40, 60, 80, 100, 120, 140, 160]
PRESET_ORDER = ["exp1", "exp2", "exp3", "exp4", "exp5"]


@dataclass
class ExperimentTask:
    preset: str
    strategy: str
    truncate_and_keep_ratio: float
    desired_num_candlesticks: int | None


def _validate_ratios(ratios: list[float]) -> None:
    if not ratios:
        raise ValueError("ratios cannot be empty.")
    for ratio in ratios:
        if ratio <= 0.0 or ratio > 1.0:
            raise ValueError(f"ratio must be in (0, 1], got {ratio}.")


def _validate_candles(candles: list[int]) -> None:
    if not candles:
        raise ValueError("gru candle list cannot be empty.")
    for candle in candles:
        if candle <= 0:
            raise ValueError(f"candle count must be > 0, got {candle}.")


def build_preset_tasks(
    preset: str,
    *,
    ratios_override: list[float] | None = None,
    gru_candles_override: list[int] | None = None,
) -> list[ExperimentTask]:
    if preset not in PRESET_ORDER:
        raise ValueError(f"Unsupported preset: {preset}")

    ratios = ratios_override if ratios_override is not None else DEFAULT_RATIO_SWEEP
    _validate_ratios(ratios)

    default_candles = gru_candles_override[0] if gru_candles_override else DEFAULT_GRU_CANDLES
    if default_candles <= 0:
        raise ValueError("gru candle count must be > 0.")

    tasks: list[ExperimentTask] = []

    if preset == "exp1":
        tasks.append(
            ExperimentTask(
                preset="exp1",
                strategy="gru",
                truncate_and_keep_ratio=ratios[0] if ratios_override else 0.67,
                desired_num_candlesticks=default_candles,
            )
        )

    elif preset == "exp2":
        tasks.append(
            ExperimentTask(
                preset="exp2",
                strategy="tabular",
                truncate_and_keep_ratio=ratios[0] if ratios_override else 0.67,
                desired_num_candlesticks=None,
            )
        )

    elif preset in {"exp3", "exp5"}:
        ratio_sweep = ratios_override if ratios_override else DEFAULT_RATIO_SWEEP
        for ratio in ratio_sweep:
            tasks.append(
                ExperimentTask(
                    preset=preset,
                    strategy="gru",
                    truncate_and_keep_ratio=ratio,
                    desired_num_candlesticks=default_candles,
                )
            )
            tasks.append(
                ExperimentTask(
                    preset=preset,
                    strategy="tabular",
                    truncate_and_keep_ratio=ratio,
                    desired_num_candlesticks=None,
                )
            )

    elif preset == "exp4":
        candle_sweep = gru_candles_override if gru_candles_override else DEFAULT_EXP4_CANDLE_SWEEP
        _validate_candles(candle_sweep)
        ratio = ratios[0] if ratios_override else 0.67
        for candle_count in candle_sweep:
            tasks.append(
                ExperimentTask(
                    preset="exp4",
                    strategy="gru",
                    truncate_and_keep_ratio=ratio,
                    desired_num_candlesticks=candle_count,
                )
            )

    return tasks
