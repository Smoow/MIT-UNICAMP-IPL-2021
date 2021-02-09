def prime(x):
    """
    Checks whether input is a prime number.

    Args:
        x [int]: numerical argument to be checked for primeness.

    Returns:
        bool representing whether x is a prime number
    """
    if x <= 1:
        return False

    if x == 2:
        return True

    if x % 2 == 0:  # todos os outros números pares não são primos
        return False

    for i in range(3, int(x ** 0.5) + 1, 2):
        # só é necessário checar os números ímpares até raiz de x (por simetria),
        # começamos em 3 e vamos de 2 em 2 (3, 5, 7, 9, ...)
        if x % i == 0:
            return False

    return True
