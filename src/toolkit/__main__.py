import argparse
import sys

from .calculator import calculate
from .converter import convert
from .errors import CalculatorError, ConversionError


def format_number(value: float) -> str:
    """Убирает .0 у целых чисел, оставляет дробные как есть."""
    if value == int(value):
        return str(int(value))
    return str(value)

def main():
    parser = argparse.ArgumentParser(
        prog='toolkit',
        description='Консольный набор утилит: калькулятор и конвертер.',
        epilog='Пример: python -m toolkit calc "2 + 3 * 4"',
    )
    sub = parser.add_subparsers(
        dest='command',
        required=True,
        title='команды',
        description='доступные подкоманды',
    )

    calc = sub.add_parser(
        'calc',
        help='вычислить арифметическое выражение',
        description='Вычисляет выражение с операторами + - * / и скобками а также // и %. Поддерживаются унарные + и -.',
    )
    calc.add_argument(
        'expression',
        help='выражение, например "2 + 3 * 4"',
    )

    conv = sub.add_parser(
        'convert',
        help='конвертировать величину',
        description='Конвертирует значение между единицами длины, массы или температуры.',
    )
    conv.add_argument(
        'value',
        type=float,
        help='числовое значение',
    )
    conv.add_argument(
        '--from',
        dest='from_unit',
        required=True,
        metavar='UNIT',
        help='исходная единица: mm, cm, m, km, g, kg, c, f, k',
    )
    conv.add_argument(
        '--to',
        dest='to_unit',
        required=True,
        metavar='UNIT',
        help='целевая единица: mm, cm, m, km, g, kg, c, f, k',
    )

    args = parser.parse_args()

    try:
        if args.command == 'calc':
            print(format_number(calculate(args.expression)))
        elif args.command == 'convert':
            print(convert(args.value, args.from_unit, args.to_unit))
        sys.exit(0)
    except (CalculatorError, ConversionError) as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == '__main__':
    main()