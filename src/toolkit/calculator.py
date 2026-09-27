"""Калькулятор арифметических выражений."""

from __future__ import annotations

from .errors import (
    ConsecutiveOperatorsError,
    DivisionByZeroError,
    EmptyExpressionError,
    InvalidCharacterError,
    MissingOperandError,
)


def tokenize(expression: str) -> list:
    if not expression or not expression.strip():
        raise EmptyExpressionError("Пустое выражение")

    tokens = []
    i = 0
    n = len(expression)

    while i < n:
        ch = expression[i]

        if ch.isspace():
            i += 1
            continue

        # число
        if ch.isdigit() or ch == '.':
            j = i
            while j < n and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            num_str = expression[i:j]
            try:
                tokens.append(('NUMBER', float(num_str)))
            except ValueError:
                raise InvalidCharacterError(f"Некорректное число: {num_str}")
            i = j
            continue

        # // раньше одиночного /
        if ch == '/' and i + 1 < n and expression[i + 1] == '/':
            tokens.append(('OP', '//'))
            i += 2
            continue

        if ch in '+-*/%()':
            tokens.append(('OP', ch))
            i += 1
            continue

        raise InvalidCharacterError(f"Недопустимый символ: {ch}")

    return tokens


def validate(tokens: list) -> None:
    if not tokens:
        raise EmptyExpressionError("Пустое выражение")

    binary = {'+', '-', '*', '/', '//', '%'}
    prev = None

    for typ, val in tokens:
        if typ == 'OP' and val in binary:
            misplaced = prev is None or (prev[0] == 'OP' and prev[1] in binary)
            is_unary = val in '+-' and (
                prev is None
                or (prev[0] == 'OP' and prev[1] in binary | {'('})
            )
            if misplaced and not is_unary:
                raise ConsecutiveOperatorsError("Два оператора подряд")
        prev = (typ, val)

    if tokens[-1][0] == 'OP' and tokens[-1][1] != ')':
        raise MissingOperandError("Пропущен операнд")


class Parser:
    """Рекурсивный спуск: expr -> term -> factor."""

    def __init__(self, tokens: list) -> None:
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def consume(self, expected: str | None = None):
        typ, val = self.peek()
        if expected is not None and val != expected:
            raise MissingOperandError(f"Ожидался {expected}")
        self.pos += 1
        return typ, val

    def parse(self) -> float:
        result = self.expr()
        if self.pos < len(self.tokens):
            raise InvalidCharacterError("Лишние токены")
        return result

    # + и - (низкий приоритет)
    def expr(self) -> float:
        left = self.term()
        while True:
            typ, val = self.peek()
            if typ == 'OP' and val in '+-':
                self.consume()
                right = self.term()
                left = left + right if val == '+' else left - right
            else:
                break
        return left

    # *, /, //, % (высокий приоритет)
    def term(self) -> float:
        left = self.factor()
        while True:
            typ, val = self.peek()
            if typ == 'OP' and val in ('*', '/', '//', '%'):
                self.consume()
                right = self.factor()
                if val == '*':
                    left = left * right
                elif val == '/':
                    if right == 0:
                        raise DivisionByZeroError("Деление на ноль")
                    left = left / right
                elif val == '//':
                    if right == 0:
                        raise DivisionByZeroError("Деление на ноль")
                    left = left // right
                elif val == '%':
                    if right == 0:
                        raise DivisionByZeroError("Деление на ноль")
                    left = left % right
            else:
                break
        return left

    # числа, скобки, унарные +/-
    def factor(self) -> float:
        typ, val = self.peek()

        if typ == 'OP' and val in '+-':
            self.consume()
            operand = self.factor()
            return operand if val == '+' else -operand

        if typ == 'OP' and val == '(':
            self.consume('(')
            result = self.expr()
            self.consume(')')
            return result

        if typ == 'NUMBER':
            self.consume()
            return val

        raise MissingOperandError("Ожидался операнд")


def calculate(expression: str) -> float:
    tokens = tokenize(expression)
    validate(tokens)
    return Parser(tokens).parse()