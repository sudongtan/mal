class Symbol:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{type(self).__name__}('{self.name}')"

    def __eq__(self, other):
        return type(self) == type(other) and self.name == other.name

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

    def __repr__(self):
        return f"{type(self).__name__}('{self.string_value}')"