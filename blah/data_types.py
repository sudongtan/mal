class Symbol:
    def __init__(self, name):
        self.name = name

class Integer:
    def __init__(self, string_value):
        self.string_value = string_value

    def __add__(self, other):
        return type(self)(str(int(self.string_value) + int(other.string_value)))

    def __sub__(self, other):
        return type(self)(str(int(self.string_value) - int(other.string_value)))

    def __mul__(self, other):
        return type(self)(str(int(self.string_value) * int(other.string_value)))

    def __truediv__(self, other):
        return type(self)(str(int(self.string_value) // int(other.string_value)))