import reader
import printer
from data_types import *

repl_env = {'+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: a/b}

def READ(x):
    return reader.read_str(x)

def EVAL(ast, env):

    if isinstance(ast, list):
        if ast:
            fun, *args = eval_ast(ast, env)
            result = fun(*args)
        else:
            result = ast
    else:
        result = eval_ast(ast, env)

    return result

def PRINT(x):
    return printer.pr_str(x)

def rep(x, env):
    y = READ(x)
    z = EVAL(y, env)
    w = PRINT(z)
    return w

def loop():
    env = repl_env
    while True:
        try:
            x = input("user> ")
        except EOFError:
            print('Exit')
            exit(0)
        try:
            result = rep(x, env)
        except NameError as exc:
            print("Error:", exc)
        else:    
            print(result)

def eval_ast(ast, env):
    if isinstance(ast, Symbol):
        try:
            result = env[ast.name]
        except KeyError:
            raise NameError(f"'{ast.name}' not found")

    elif isinstance(ast, list):
        result = [EVAL(item, env) for item in ast] 
    
    else:
        result = ast

    return result

if __name__ == "__main__":
    loop()