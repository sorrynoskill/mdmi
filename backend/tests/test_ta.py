import pytest

from backend.app.indicators.ta import ema, ema_21, ema_9, rsi, rsi_14


def test_ema_returns_none_until_seed_window() -> None:
    closes = [100, 101, 102, 103, 104, 105, 106, 107, 108]

    values = ema_9(closes)

    assert values[:-1] == [None] * 8
    assert values[-1] == pytest.approx(sum(closes) / len(closes))


def test_ema_uses_recursive_smoothing_after_seed() -> None:
    closes = [1, 2, 3, 4, 5]

    values = ema(closes, period=3)

    # Seed is SMA(1,2,3)=2.0, alpha=0.5 -> next values: 3.0, 4.0
    assert values == [None, None, 2.0, 3.0, 4.0]


def test_rsi_constant_uptrend_hits_100() -> None:
    closes = list(range(1, 21))

    values = rsi_14(closes)

    assert values[:14] == [None] * 14
    assert values[14:] == [100.0] * (len(closes) - 14)


def test_rsi_matches_known_reference_value() -> None:
    # Reference sequence used in RSI examples (Wilder), first RSI ~= 70.464
    closes = [
        44.34,
        44.09,
        44.15,
        43.61,
        44.33,
        44.83,
        45.10,
        45.42,
        45.84,
        46.08,
        45.89,
        46.03,
        45.61,
        46.28,
        46.28,
    ]

    values = rsi(closes, period=14)

    assert values[:-1] == [None] * 14
    assert values[-1] == pytest.approx(70.464, abs=1e-3)


def test_indicator_input_validation() -> None:
    with pytest.raises(ValueError):
        ema([1, 2, 3], period=0)

    with pytest.raises(ValueError):
        rsi([1, 2, 3], period=-1)


def test_ema_21_short_series_returns_none_only() -> None:
    closes = [1.0] * 10
    values = ema_21(closes)
    assert len(values) == len(closes)
    assert all(v is None for v in values)
