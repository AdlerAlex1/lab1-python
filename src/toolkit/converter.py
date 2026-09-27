"""Конвертер величин: длина, масса, температура.

Каждая единица принадлежит группе. Конвертация идёт через базовую
единицу группы: метры, килограммы, градусы Цельсия.
"""

from .errors import (
    BelowAbsoluteZeroError,
    IncompatibleUnitsError,
    UnknownUnitError,
)

LENGTH = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000.0}
MASS = {'g': 0.001, 'kg': 1.0}
TEMPERATURE = {'c', 'f', 'k'}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Конвертирует значение между единицами одной группы.

    Args:
        value: числовое значение.
        from_unit: исходная единица (mm, cm, m, km, g, kg, c, f, k).
        to_unit: целевая единица.

    Returns:
        Результат как float.

    Raises:
        UnknownUnitError: если единица не поддерживается.
        IncompatibleUnitsError: если единицы из разных групп.
        BelowAbsoluteZeroError: если температура ниже абсолютного нуля.
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    def group(unit: str) -> str:
        """Определяет группу единицы: length, mass или temperature."""
        if unit in LENGTH:
            return 'length'
        if unit in MASS:
            return 'mass'
        if unit in TEMPERATURE:
            return 'temperature'
        raise UnknownUnitError(f"Неизвестная единица: {unit}")

    g1 = group(from_unit)
    g2 = group(to_unit)

    if g1 != g2:
        raise IncompatibleUnitsError(
            f"Несовместимые единицы: {from_unit} и {to_unit}"
        )

    if g1 == 'length':
        return value * LENGTH[from_unit] / LENGTH[to_unit]

    if g1 == 'mass':
        return value * MASS[from_unit] / MASS[to_unit]

    # температура: сначала в Цельсий
    if from_unit == 'c':
        celsius = value
    elif from_unit == 'f':
        celsius = (value - 32) * 5 / 9
    else:  # k
        celsius = value - 273.15

    if celsius < -273.15:
        raise BelowAbsoluteZeroError("Температура ниже абсолютного нуля")

    # из Цельсия в целевую
    if to_unit == 'c':
        return celsius
    if to_unit == 'f':
        return celsius * 9 / 5 + 32
    return celsius + 273.15  # k