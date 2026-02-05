from __future__ import annotations

from collections.abc import Sequence


def ema(values: Sequence[float], period: int) -> list[float | None]:
    """Compute Exponential Moving Average (EMA) with SMA seeding.

    Returns a list with the same length as ``values``. Elements before the
    first complete window are ``None``.
    """
    if period <= 0:
        raise ValueError("period must be positive")
    if not values:
        return []
    if len(values) < period:
        return [None] * len(values)

    alpha = 2 / (period + 1)
    result: list[float | None] = [None] * len(values)

    seed = sum(values[:period]) / period
    result[period - 1] = seed
    previous = seed

    for i in range(period, len(values)):
        current = (values[i] - previous) * alpha + previous
        result[i] = current
        previous = current

    return result


def rsi(values: Sequence[float], period: int = 14) -> list[float | None]:
    """Compute RSI using Wilder's smoothing method."""
    if period <= 0:
        raise ValueError("period must be positive")
    if not values:
        return []
    if len(values) <= period:
        return [None] * len(values)

    result: list[float | None] = [None] * len(values)

    gains: list[float] = []
    losses: list[float] = []
    for i in range(1, period + 1):
        delta = values[i] - values[i - 1]
        gains.append(max(delta, 0.0))
        losses.append(max(-delta, 0.0))

    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period

    if avg_loss == 0:
        result[period] = 100.0
    else:
        rs = avg_gain / avg_loss
        result[period] = 100 - (100 / (1 + rs))

    for i in range(period + 1, len(values)):
        delta = values[i] - values[i - 1]
        gain = max(delta, 0.0)
        loss = max(-delta, 0.0)

        avg_gain = ((avg_gain * (period - 1)) + gain) / period
        avg_loss = ((avg_loss * (period - 1)) + loss) / period

        if avg_loss == 0:
            result[i] = 100.0
        else:
            rs = avg_gain / avg_loss
            result[i] = 100 - (100 / (1 + rs))

    return result


def ema_9(values: Sequence[float]) -> list[float | None]:
    return ema(values, period=9)


def ema_21(values: Sequence[float]) -> list[float | None]:
    return ema(values, period=21)


def rsi_14(values: Sequence[float]) -> list[float | None]:
    return rsi(values, period=14)
