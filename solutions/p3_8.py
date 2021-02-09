def composite_result(f, g, x):
    """
    Calculates the composite result, f(g(x))

    Args:
        f: external function
        g: internal function
        x: value to which we apply the functions

    Returns:
        composite result, f(g(x))
    """
    return f(g(x))


def composite(f, g):
    """
    Generates a function that takes in x and returns f(g(x))

    Args:
        f: external function
        g: internal function

    Returns:
        function object
    """
    return lambda x: f(g(x))