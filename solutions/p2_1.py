def square(x):
    """
    Calculate the square of a number.

    Args:
        x [int, float]: numerical argument to be squared.

    Returns:
        Square of x.
    """
    return x ** 2
    

def fourth_power(x):
    """
    Calculate the fourth power of a number.
    
    Args:
        x [int, float]: numerical argument to be exponentiated.
        
    Returns:
        Fourth power of x.
    """
    return square(square(x))


def perfect_square(x):
    """
    Checks whether x is a perfect square. May fail for significantly large
    non-square integer inputs.

    Args:
        x [int, float]: nonnegative numerical argument to check.

    Returns:
        bool representing whether x is a perfect square
    """
    if x < 0:
        raise ValueError("Input must be positive")

    sqrt = x ** 0.5
    # se x é um quadrado perfeito, sua raiz já é um inteiro, então truncar
    # sqrt com int() leva ao mesmo número e a diferença é zero
    return (sqrt - int(sqrt)) == 0
