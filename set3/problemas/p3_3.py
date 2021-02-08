def dictmap(d, f):
    for key in d:
        d[key] = f(d[key])

    return

def f(x):
    return x * x
