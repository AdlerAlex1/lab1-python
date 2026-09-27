import pytest

from toolkit.calculator import calculate
from toolkit.errors import (
    EmptyExpressionError,
    InvalidCharacterError,
    MissingOperandError,
    ConsecutiveOperatorsError,
    DivisionByZeroError,
)


# ---------- Позитивные ----------

def test_addition():
    assert calculate("2 + 3") == 5.0


def test_subtraction():
    assert calculate("10 - 4") == 6.0


def test_multiplication():
    assert calculate("3 * 4") == 12.0


def test_division():
    assert calculate("10 / 4") == 2.5


def test_priority():
    #Умножение должно выполняться раньше сложения
    assert calculate("2 + 3 * 4") == 14.0


def test_parentheses():
    assert calculate("(2 + 3) * 4") == 20.0


def test_unary_minus():
    assert calculate("-5 + 3") == -2.0


def test_unary_plus():
    assert calculate("+5 + 3") == 8.0


def test_float_numbers():
    assert calculate("1.5 * 2") == 3.0


def test_spaces_ignored():
    assert calculate("  2   +   3  ") == 5.0


# ---------- Негативные ----------

def test_empty_expression():
    with pytest.raises(EmptyExpressionError):
        calculate("")


def test_whitespace_only():
    with pytest.raises(EmptyExpressionError):
        calculate("   ")


def test_invalid_character():
    with pytest.raises(InvalidCharacterError):
        calculate("2 & 3")


def test_consecutive_operators():
    with pytest.raises(ConsecutiveOperatorsError):
        calculate("2 * * 3")


def test_missing_operand_at_end():
    with pytest.raises(MissingOperandError):
        calculate("2 +")


def test_division_by_zero():
    with pytest.raises(DivisionByZeroError):
        calculate("1 / 0")


def test_division_by_zero_in_parentheses():
    with pytest.raises(DivisionByZeroError):
        calculate("5 / (3 - 3)")

#---------- Дополнительные тесты для // ----------
def test_floor_division():
    assert calculate("10 // 3") == 3.0

def test_floor_division_precedence():
    assert calculate("2 + 10 // 3") == 5.0


def test_floor_division_by_zero():
    with pytest.raises(DivisionByZeroError):
        calculate("10 // 0")

# =========== Дополнительные тесты для % ==========
def test_modulo_by_zero():
    with pytest.raises(DivisionByZeroError):
        calculate("10 % 0")


def test_negative_floor_division():
    assert calculate("-10 // 3") == -4.0


def test_negative_modulo():
    assert calculate("-10 % 3") == 2.0
