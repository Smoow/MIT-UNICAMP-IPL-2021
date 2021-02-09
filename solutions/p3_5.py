def approx_derivative(f, x, delta=1e-6):
    """
    Calculates approximate derivative value at x for function f
    Args:
        f: function being considered
        x: point being considered
        delta: half the small interval's length used to linearly approximate the derivative

    Returns:
        Approximate derivative of f at point x
    """
    # fórmula fornecida na página do exercício
    return (f(x+delta) - f(x-delta)) / (2*delta)


def approx_derivative_2(f, delta=1e-6):
    """
    Generates function that takes a value x and gives the approximate
    derivative value at x for function f

    Args:
        f: function being considered
        delta: half the small interval's length used to linearly approximate the derivative

    Returns:
        Function that takes x and gives approximate derivative of f at x
    """
    def inner(x):  # função a ser retornada
        return approx_derivative(f, x, delta)

    return inner  # poderia ter feito return lambda x: approx_derivative(f, x, delta)


def approx_integral(f, lo, hi, num_regions):
    """
    Calculates approximate integral of function f over [lo, hi] interval using
    the trapezoidal rule

    Args:
        f: function being considered
        lo: beginning of integration interval
        hi: end of integration interval
        num_regions: number of regions to break the interval into for approximation.

    Returns:
        Approximate integral of f over [lo, hi]
    """
    step = (hi - lo) / num_regions  # tamanho de cada segmento
    total = 0

    total += f(lo) / 2  # primeiro termo, primeiro ponto

    for i in range(1, num_regions):
        total += f(lo + i*step)

    total += f(hi) / 2  # último termo, último ponto

    return total * step
