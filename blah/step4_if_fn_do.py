import reader
import printer
from data_types import *
from env import Env
import core


repl_env = Env(None)


def READ(x):
    return reader.read_str(x)


def EVAL(ast, env):

    if isinstance(ast, list):
        #print(ast)
        if ast:
            if isinstance(ast[0], Symbol):
                if ast[0].name == 'def!':
                    _, key, value = ast
                    evaluated = EVAL(value, env)
                    env.set(key.name, evaluated)
                    result = env.get(key.name)

                elif ast[0].name == 'let*':
                    _, bindings, expr = ast
                    env_let = Env(env)
                    for symbol, value in zip(bindings[:-1:2], bindings[1::2]):
                        #print(env_let)
                        evaluated = EVAL(value, env_let)
                        env_let.set(symbol.name, evaluated)
                    
                    result = EVAL(expr, env_let)

                elif ast[0].name == 'do':
                    result = eval_ast(ast[1:], env)[-1]
                    
                elif ast[0].name == 'if':
                    _, condition, *branches = ast
                    evaluated_condition = EVAL(condition, env)
                    if evaluated_condition not in [Nil(), Bool('false')]:
                        result = EVAL(branches[0], env)
                    else:
                        if len(branches) > 1:
                            result = EVAL(branches[1], env)
                        else:
                            result = Nil()

                elif ast[0].name == 'fn*':
                    def func(*params):
                        new_env = Env(env, ast[1], params)
                        return EVAL(ast[2], new_env)
                    result = func 
                else:
                    fun, *args = eval_ast(ast, env)
                    result = fun(*args)
            else:
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
        except KeyError as exc:
            print("Error:", exc)
        else:    
            print(result)

def eval_ast(ast, env):
    #print(env)
    if isinstance(ast, Symbol):
        result = env.get(ast.name)

    elif isinstance(ast, list):
        result = [EVAL(item, env) for item in ast] 
    
    else:
        result = ast

    return result

if __name__ == "__main__":
    for key, value in core.ns.items():
        repl_env.set(key, value)
    rep("(def! not (fn* (a) (if a false true)))", repl_env)
    loop()
