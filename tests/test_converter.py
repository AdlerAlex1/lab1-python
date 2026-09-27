import pytest

from toolkit.converter import convert
from toolkit.errors import (
    BelowAbsoluteZeroError,
    IncompatibleUnitsError,
    UnknownUnitError,
)

# ---------- Позитивные ----------

def test_length_m_to_cm():
    assert convert(1, "m", "cm") == 100.0


def test_length_km_to_mm():
    assert convert(1, "km", "mm") == 1_000_000.0


def test_mass_kg_to_g():
    assert convert(1, "kg", "g") == 1000.0


def test_temperature_c_to_f():
    assert convert(0, "c", "f") == 32.0


def test_temperature_c_to_k():
    assert convert(0, "c", "k") == pytest.approx(273.15)


def test_case_insensitive_units():
    assert convert(1, "M", "CM") == 100.0


# ---------- Негативные ----------

def test_unknown_unit():
    with pytest.raises(UnknownUnitError):
        convert(1, "m", "xyz")


def test_unknown_from_unit():
    with pytest.raises(UnknownUnitError):
        convert(1, "foo", "m")


def test_incompatible_units():
    with pytest.raises(IncompatibleUnitsError):
        convert(1, "m", "kg")


def test_below_absolute_zero():
    with pytest.raises(BelowAbsoluteZeroError):
        convert(-300, "c", "k")