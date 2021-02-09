def binary_tree_max(tree):
    if (len(tree['children']) == 0):
        return tree['value']

    large_number = tree['value']

    for i in tree['children']:
        tmp_large_number = binary_tree_max(i)

        if tmp_large_number > large_number:
            large_number = tmp_large_number

    return large_number


def tree_max(tree):
    if (len(tree['children']) == 0):
        return tree['value']

    large_number = tree['value']

    for child in tree['children']:
        tmp_large_number = tree_max(child)

        if tmp_large_number > large_number:
            large_number = tmp_large_number

    return large_number
