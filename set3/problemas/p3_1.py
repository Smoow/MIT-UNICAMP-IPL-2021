def join_arrays(array):
    """
        Returns a joint of any arrays to a single one
    """
    out = []
    for i in array:
        for j in i:
            out.append(j)

    out.append(None)
    return out


def run_length_encode_2d(array):
    joined_array = join_arrays(array)
    array_length = len(joined_array)
    counter_index = 1
    actual = 0
    counter = 1
    out = []

    while (counter_index < array_length):
        if joined_array[actual] == joined_array[counter_index]:
            counter += 1
        else:
            out.append((counter, joined_array[actual]))
            actual += counter
            counter = 1
        counter_index += 1

    return out
