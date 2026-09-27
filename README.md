

# Toolkit

Консольный набор утилит: калькулятор выражений(через recursive descent) и конвертер величин.

## Установка

```bash
python3 -m venv .venv
source .venv/bin/activate    # Windows(CMD): .venv\Scripts\activate.bat
pip install -e ".[dev]" # Кавычки вокруг ".[dev]" обязательны — иначе shell неправильно передаст аргумент.
```

## Использование

### Калькулятор

```bash
python -m toolkit calc "2 + 3 * 4"
# 14

python -m toolkit calc "(2 + 3) * 4"
# 20

python -m toolkit calc "10 // 3"
# 3

python -m toolkit calc "10 % 3"
# 1
```

Поддерживаются: `+`, `-`, `*`, `/`, `//`, `%`, скобки, унарные `+` и `-`.
Соблюдены приоритеты операций.

Если выражение начинается с `-`, ставьте `--`(опционально):

```bash
python -m toolkit calc -- "-5 + 3"
# -2
```

### Конвертер

```bash
python -m toolkit convert 1 --from m --to cm
# 100.0

python -m toolkit convert 1 --from kg --to g
# 1000.0

python -m toolkit convert 0 --from c --to f
# 32.0
```

### Справка

```bash
python -m toolkit --help
python -m toolkit calc --help
python -m toolkit convert --help
```

## Единицы

| Группа | Единицы |
|---|---|
| Длина | `mm`, `cm`, `m`, `km` |
| Масса | `g`, `kg` |
| Температура | `c`, `f`, `k` |

Регистр не учитывается. Конвертация между разными группами запрещена.
Температура ниже абсолютного нуля не поддерживается.

## Ошибки
Обрабатываемые ошибки

Ошибка ----------------------------	Исключение
Пустое выражение	                  EmptyExpressionError
Недопустимый символ	                InvalidCharacterError
Пропущен операнд	                  MissingOperandError
Два бинарных оператора подряд	      ConsecutiveOperatorsError
Деление на ноль (/, //, %)	        DivisionByZeroError
Неизвестная единица	                UnknownUnitError
Несовместимые единицы	              IncompatibleUnitsError
Температура ниже абсолютного нуля	  BelowAbsoluteZeroError
Неверное числовое значение	        InvalidNumericValueError


Все исключения наследуются от ToolkitError (для калькулятора — CalculatorError,
для конвертера — ConversionError)

Ошибки выводятся в stderr, код возврата — `2`. Успех — `0`.

## проверка ошибок и "чистоты кода"

```bash
python -m pytest -v #проверка работоспособности 37 тестов 
ruff check . 
```

## Структура

```
src/toolkit/
  __main__.py      # CLI
  calculator.py    # калькулятор
  converter.py     # конвертер
  errors.py        # исключения
tests/
  test_calculator.py
  test_converter.py
  test_cli.py
```
