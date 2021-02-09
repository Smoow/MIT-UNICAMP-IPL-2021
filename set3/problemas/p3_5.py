def approx_derivative(f, x, delta=1e-6):
    derivative = (f(x+delta) - f(x-delta)) / (2*delta)
    return derivative
    

def approx_derivative_2(f, delta=1e-6):
    def f_line(x):
        derivative = (f(x+delta) - f(x-delta)) / (2*delta)
        return derivative
    return f_line


def approx_integral(f, lo, hi, num_regions):
    h = float(hi - lo) / num_regions
    s = 0.0
    s += f(lo) / 2.0

    for i in range(1, num_regions):
        s += f(lo + i*h)

    s += f(hi) / 2.0
    return s * h


def f(x):
    return x * x
