def run_length_encode_2d(array):
    """
    Implements run-length encoding in a 2d-array represented as list of lists.

    Args:
        array: nested list representation of 2d-array

    Returns:
        list of tuples yielding run length encoded data version
    """
    out = []
    # current manterá uma lista de dois elementos: [elemento, contagem]
    # que armazena qual o último elemento visto e quantas vezes seguidas o vimos
    current = None

    for inner_array in array:
        for elem in inner_array:
            if current is None:
                # apenas primeiro elemento passa por aqui; inicializa o termo current
                current = [1, elem]
            elif current[1] == elem:
                # se o valor visto (elem) é o mesmo que temos em current, apenas
                # adicionamos um à contagem e seguimos
                current[0] += 1
            else:
                # se o valor é diferente, o termo current precisa trocar. Adicionamos
                # o antigo à lista resultado e inicializamos um novo current
                out.append(tuple(current))
                current = [1, elem]

    out.append(tuple(current))  # não esqueça do último elemento!

    return out
