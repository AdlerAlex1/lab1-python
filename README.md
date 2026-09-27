
# Toolkit

Консольный набор утилит: калькулятор выражений и конвертер величин.

## Установка

```bash
python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -e ".[dev]" #Кавычки вокруг ".[dev]" обязательны — иначе shell неправильно передаст аргумент.
```

## Использование

### Калькулятор

```bash
python -m toolkit calc "2 + 3 * 4"
# 14.0

python -m toolkit calc "(2 + 3) * 4"
# 20.0

python -m toolkit calc "10 // 3"
# 3.0

python -m toolkit calc "10 % 3"
# 1.0
```

Поддерживаются: `+`, `-`, `*`, `/`, `//`, `%`, скобки, унарные `+` и `-`.

Если выражение начинается с `-`, ставьте `--`:

```bash
python -m toolkit calc -- "-5 + 3"
# -2.0
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

## Ошибки

Ошибки выводятся в stderr, код возврата — `2`. Успех — `0`.

## проверка ошибок и чистоты кода

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

