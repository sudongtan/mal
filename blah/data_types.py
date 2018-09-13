class Symbol:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if type(self)==type(other) and self.name==other.name:
            return Bool('true')
        else:
            return Bool('false')


class Integer:
    def __init__(self, string_value):
        self.string_value = string_value

    def __eq__(self, other):
        if type(self) == type(other) and int(self.string_value) == int(other.string_value):
            return Bool('true')
        else:
            return Bool('false')

    def __add__(self, other):
        return type(self)(str(int(self.string_value) + int(other.string_value)))

    def __sub__(self, other):
        return type(self)(str(int(self.string_value) - int(other.string_value)))

    def __mul__(self, other):
        return type(self)(str(int(self.string_value) * int(other.string_value)))

    def __truediv__(self, other):
        return type(self)(str(int(self.string_value) // int(other.string_value)))

    def __lt__(self, other):
        if type(self) == type(other) and int(self.string_value) < int(other.string_value):
            return Bool('true')
        else:
            return Bool('false')

    def __gt__(self, other):
        if type(self) == type(other) and int(self.string_value) > int(other.string_value):
            return Bool('true')
        else:
            return Bool('false')

    def __repr__(self):
        return self.string_value


class Nil:
    def __eq__(self, other):
        if type(self) == type(other):
            return Bool('true')
        else:
            return Bool('false')
        
    def __repr__(self):
        return "nil"

    def __len__(self):
        return 0

class Bool:
    def __init__(self, value):
        if value not in ['true', 'false']:
            raise ValueError
        self.value = value

    def __eq__(self, other):
        if type(self) == type(other) and self.value == other.value:
            return Bool('true')
        else:
            return Bool('false')

    def __bool__(self):
        return self.value == 'true'

    def __repr__(self):
        return self.value

# class Function:
#     def __init__(self)

# NIL = Nil()
# TRUE = 