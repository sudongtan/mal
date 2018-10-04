from data_types import Symbol
from itertools import zip_longest

class Env:
    def __init__(self, outer, binds=None, exprs=None):
        self.outer = outer
        self.data = {}
        if binds:
            for i, (bind, expr) in enumerate(zip_longest(binds, exprs)):
                if bind == Symbol("&"):
                    self.set(binds[i + 1].name, list(exprs[i:]))
                    break
                else:
                    self.set(bind.name, expr)

    def set(self, key, value):
        #print(key, value, type(value))
        self.data[key] = value

    def find(self, key):
        #print(self.data, key, type(key))
        if key in self.data:
            return self #??

        else:
            if self.outer: #??
                return self.outer.find(key)

            else:
                return None

    def get(self, key):
        environment = self.find(key)
        if environment:
            return environment.data[key]

        else:
            raise KeyError(f"'{key}' not found")

    def __repr__(self):
        return f"{type(self).__name__}({self.data}, outer={self.outer})"