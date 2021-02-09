def hailstone_sequence(a_0):
    """
    Generates the hailstone sequence when starting from a_0 up to first 1 value.
    Assumes the Collatz conjecture.

    Args:
        a_0: initial value of the hailstone sequence being explored.

    Returns:
        list containing the hailstone sequence up to first 1 value
    """
    value = a_0
    out = []

    while value != 1:
        out.append(value)

        if value % 2 == 0:  # caso par
            value = int(value / 2)
        else:  # caso ímpar
            value = 3 * value + 1

    out.append(value)  # não esqueça do último valor!

    return out
