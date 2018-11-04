from data_types import Symbol
from itertools import zip_longest

class Env:
    def __init__(self, outer, binds=None, exprs=None):
        self.outer = outer
        self.data = {}
        if binds:
            # print('binds', binds, 'exprs', exprs)
            for i, bind in enumerate(binds):
                if bind == Symbol("&"):
                    self.set(binds[i + 1].name, list(exprs[i:]))
                    break
                else:
                    self.set(bind.name, exprs[i])

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
        #return f"{type(self).__name__}({list(self.data)}, outer={self.outer})"
        return f"{type(self).__name__}(..., outer={self.outer})"