def composite_result(f, g, x):
    return f(g(x))

def composite(f, g):
    def fog(x):
        return f(g(x))
    return fog

def f(x):
    return x * x

def g(x):
    return x + 2
