from data_types import Symbol

class Env:
    def __init__(self, outer, binds=None, exprs=None):
        self.outer = outer
        self.data = {}
        if binds and exprs:
            for i, (bind, expr) in enumerate(zip(binds, exprs)):
                if bind == Symbol("&"):
                    self.set(binds[i + 1].name, exprs[i:])
                    break
                else:
                    self.set(bind.name, expr)

    def set(self, key, value):
        self.data[key] = value

    def find(self, key):
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