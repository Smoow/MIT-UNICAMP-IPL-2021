def swap(d, k1, k2):
    """
    Swaps the values bound to keys k1, k2 in dictionary d
    Args:
        d: dict
        k1, k2: keys from d

    Returns:
        None
    """
    # variáveis temporárias são um jeito de trocar dois valores
    value1 = d[k1]
    value2 = d[k2]

    d[k1] = value2
    d[k2] = value1
    # alternativamente, d[k1], d[k2] = d[k2], d[k1] faz o mesmo que o código acima
