def ndoors(n):
    """
    Solves the n-doors, n-passes problem. All start locked and the sequence
    is 1-indexed.

    Args:
        n: number of doors/passes to be made.

    Returns:
        a list containing the indices of doors unlocked after n passes, where
        numbers are 1-indexed.
    """
    # False indica porta trancada, True porta aberta
    doors = [False] * n

    for m in range(1, n + 1):
        for k in range(n):
            if (k + 1) % m == 0:
                doors[k] = not doors[k]

    result = []
    for index, door_state in enumerate(doors):
        if door_state:
            result.append(index + 1)
    # Alternativamente:
    # result = [ind + 1 for ind in range(len(doors)) if doors[ind]]

    return result
