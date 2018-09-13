from printer import *

def prn(content):
    print(pr_str(content, print_readably=True))
    return Nil()

def ls(*params):
    return list(params)


ns = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    'prn': prn,
    'list': ls,
    'list?': lambda x: Bool('true') if isinstance(x, list) else Bool('false'),
    'empty?': lambda x: Bool('true') if not x else Bool('false'),
    'count': lambda x: Integer(str(len(x))),
    '=': lambda a, b: Bool('true') if a == b else Bool('false'),
    '<': lambda a, b: Bool('true') if a < b else Bool('false'),
    '>': lambda a, b: Bool('true') if a > b else Bool('false'),
    '>=': lambda a, b: Bool('true') if (a == b) or (a > b) else Bool('false'),
    '<=': lambda a, b: Bool('true') if (a == b) or (a < b) else Bool('false'),


}



