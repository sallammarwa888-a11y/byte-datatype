"""Tryte: a tiny wrapping integer type with a 0..26 range."""

__all__ = ["Tryte"]
__version__ = "1.0.0"


class Tryte:
    """An integer-like value that wraps in base 27."""

    MOD = 27

    def __init__(self, value=0):
        if isinstance(value, Tryte):
            value = value.value
        if not isinstance(value, int):
            raise TypeError("Tryte value must be an int")
        self.value = value % self.MOD

    def __int__(self):
        return self.value

    def __repr__(self):
        return f"Tryte({self.value})"

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, Tryte):
            return self.value == other.value
        if isinstance(other, int):
            return self.value == other % self.MOD
        return NotImplemented

    def _coerce_other(self, other):
        if isinstance(other, Tryte):
            return other.value
        if isinstance(other, int):
            return other
        return NotImplemented

    def __add__(self, other):
        other = self._coerce_other(other)
        if other is NotImplemented:
            return NotImplemented
        return Tryte(self.value + other)

    def __sub__(self, other):
        other = self._coerce_other(other)
        if other is NotImplemented:
            return NotImplemented
        return Tryte(self.value - other)

    def __mul__(self, other):
        other = self._coerce_other(other)
        if other is NotImplemented:
            return NotImplemented
        return Tryte(self.value * other)

    def __floordiv__(self, other):
        other = self._coerce_other(other)
        if other is NotImplemented:
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError("division by zero")
        return Tryte(self.value // other)

    def __mod__(self, other):
        other = self._coerce_other(other)
        if other is NotImplemented:
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError("integer modulo by zero")
        return Tryte(self.value % other)

    def __neg__(self):
        return Tryte(-self.value)

    def __iadd__(self, other):
        result = self + other
        if result is NotImplemented:
            return NotImplemented
        self.value = result.value
        return self

    def __isub__(self, other):
        result = self - other
        if result is NotImplemented:
            return NotImplemented
        self.value = result.value
        return self
