def largest_number(input_list):
    """
    Retrieves the largest number in the input list.

    Args:
        input_list [iterable]: iterable containing numbers

    Returns:
        largest number in input iterable; None if input is empty
    """
    best_so_far = None  # já cuida do caso de lista vazia

    for elem in input_list:
        if best_so_far is None or elem > best_so_far:
            # primeiro número sempre será colocado (já que best_so_far era None)
            # e a partir daí só será trocado por números maiores
            best_so_far = elem

    return best_so_far


def second_largest_number(input_list):
    """
    Retrieves the second largest number in the input list.

    Args:
        input_list [iterable]: iterable containing numbers

    Returns:
        second largest number in input iterable;
        None if input has less than two elements
    """
    if len(input_list) < 2:
        return None

    m1 = float("-inf")  # contém maior número visto
    m2 = float("-inf")  # contém segundo maior número visto

    for num in input_list:
        if num > m2:
            if num >= m1:
                # essas duas linhas podem ser trocadas por m1, m2 = num, m1
                m2 = m1
                m1 = num
            else:
                m2 = num

    return m2
