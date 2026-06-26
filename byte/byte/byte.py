class Byte(int):
    def __new__(cls, value=0):
        return int.__new__(cls, value & 0xFF)  # keep only 8 bits

    def __repr__(self):
        return f"Byte({int(self)})"

    def __str__(self):
        return str(int(self))

    def __add__(self, other):
        return Byte(int(self) + int(other))

    def __sub__(self, other):
        return Byte(int(self) - int(other))

    def __mul__(self, other):
        return Byte(int(self) * int(other))

    def __floordiv__(self, other):
        return Byte(int(self) // int(other))

    def __and__(self, other):
        return Byte(int(self) & int(other))

    def __or__(self, other):
        return Byte(int(self) | int(other))

    def __xor__(self, other):
        return Byte(int(self) ^ int(other))

    def __invert__(self):
        return Byte(~int(self))

    def __lshift__(self, bits):
        return Byte(int(self) << int(bits))

    def __rshift__(self, bits):
        return Byte(int(self) >> int(bits))