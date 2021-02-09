def dictmap(d, f):
    """
    Maps function f to all values in dict d.

    Args:
        d: dict whose values are to be mapped
        f: function to be applied

    Returns:
        None
    """
    for key in d:
        # aplica a função para cada valor (d[key]) do dicionário e liga a
        # mesma chave ao resultado de chamar a função
        d[key] = f(d[key])
