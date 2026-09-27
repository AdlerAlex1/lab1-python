class CalculatorError(Exception):
    pass

class EmptyExpressionError(CalculatorError):
    pass

class InvalidCharacterError(CalculatorError):
    pass

class MissingOperandError(CalculatorError):
    pass

class ConsecutiveOperatorsError(CalculatorError):
    pass

class DivisionByZeroError(CalculatorError):
    pass

class ConversionError(Exception):
    pass

class UnknownUnitError(ConversionError):
    pass

class IncompatibleUnitsError(ConversionError):
    pass

class BelowAbsoluteZeroError(ConversionError):
    pass

class InvalidNumericValueError(ConversionError):
    pass