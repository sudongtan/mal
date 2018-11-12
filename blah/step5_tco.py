from collections import namedtuple

import reader
import printer
from data_types import *
from env import Env
import core


class Func(namedtuple('Func', ["ast", "params", "env", "fn"])):
    def __repr__(self):
        inside = '\n  '.join(f'{k}={v}' for k, v in self._asdict().items())
        return f"{type(self).__name__}(\n  {inside})"

repl_env = Env(None)


def READ(x):
    return reader.read_str(x)

def EVAL(ast, env):
    
    while True:
        if not isinstance(ast, list):
            return eval_ast(ast, env)
        
        if not ast:
            return ast

        name = getattr(ast[0], 'name', None)

        if name == 'def!':
            _, key, value = ast
            evaluated = EVAL(value, env)
            env.set(key.name, evaluated)
            result = env.get(key.name)

        elif name == 'let*':
            _, bindings, expr = ast
            env_let = Env(env)
            for symbol, value in zip(bindings[:-1:2], bindings[1::2]):
                #print(env_let)
                evaluated = EVAL(value, env_let)
                env_let.set(symbol.name, evaluated)
            
            #result = EVAL(expr, env_let)
            env = env_let
            ast = expr
            continue
            
        elif name == 'do':
            #result = eval_ast(ast[1:], env)[-1]
            result = eval_ast(ast[1:-1], env)[-1]
            ast = ast[-1]
            continue
            
        elif name == 'if':
            _, condition, *branches = ast
            evaluated_condition = EVAL(condition, env)
            if evaluated_condition not in [Nil(), Bool('false')]:
                #result = EVAL(branches[0], env)
                ast = branches[0]
                
            else:
                if len(branches) > 1:
                    #result = EVAL(branches[1], env)
                    ast = branches[1]

                else:
                    #result = Nil()
                    ast = Nil()
            continue
            #return result

        elif name == 'fn*':
            _, param_names, body = ast
            def func(*param_values):
                new_env = Env(env, param_names, param_values)
                return EVAL(body, new_env)
            result = Func(ast=body, 
                          params=param_names, 
                          env=env, 
                          fn=func)

        else:
            fun, *param_values = eval_ast(ast, env)
            if isinstance(fun, Func):
                new_env = Env(fun.env, fun.params, param_values)
                ast = fun.ast
                env = new_env
                continue
            else:
                result = fun(*param_values)
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
    