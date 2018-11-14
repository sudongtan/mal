from printer import *
from reader import *

def prn(*args):
    #print(pr_str(content, print_readably=True))
    print(" ".join(pr_str(arg, print_readably=True) for arg in args))
    return Nil()

def ls(*params):
    return list(params)

def println(*args):
    print(" ".join(pr_str(arg, print_readably=False) for arg in args))
    return Nil()

def minus(a, b):
    return a - b

def slurp(filename):
    with open(filename.value, 'r') as f:
        return String(f.read())

ns = {
    '+': lambda a, b: a + b,
    '-': minus,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    'list': ls,
    'list?': lambda x: Bool('true') if isinstance(x, list) else Bool('false'),
    'empty?': lambda x: Bool('true') if not x else Bool('false'),
    'count': lambda x: Integer(str(len(x))),
    '=': lambda a, b: Bool('true') if a == b else Bool('false'),
    '<': lambda a, b: Bool('true') if a < b else Bool('false'),
    '>': lambda a, b: Bool('true') if a > b else Bool('false'),
    '>=': lambda a, b: Bool('true') if (a == b) or (a > b) else Bool('false'),
    '<=': lambda a, b: Bool('true') if (a == b) or (a < b) else Bool('false'),
    'pr-str': lambda *args: String(" ".join(pr_str(arg, print_readably=True) for arg in args)),
    'str': lambda *args: String("".join(pr_str(arg, print_readably=False) for arg in args)),
    'prn': prn,
    'println': println,
    'read-string': lambda s: read_str(s.value),
    'slurp': slurp,
}



