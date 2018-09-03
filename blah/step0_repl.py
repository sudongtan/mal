def READ(x):
    return x

def EVAL(x):
    return x

def PRINT(x):
    return x

def rep(x):
    y = READ(x)
    z = EVAL(y)
    w = PRINT(z)
    return w

def loop():
    while True:
        try:
            x = input("user> ")
        except EOFError:
            print('Exit')
            exit(0)
        result = rep(x)
        print(result)

if __name__ == "__main__":
    loop()