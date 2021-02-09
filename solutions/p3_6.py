def tree_max(tree):
    """
    Finds the maximum value in an arbitrary tree.

    Args:
        tree: dict representation of an arbitrary tree where nodes have numerical values

    Returns:
        maximum node value of tree
    """
    # Caso base da recursão: node sem filhos
    if len(tree['children']) == 0:
        return tree['value']

    # Caso recursivo: melhor valor no começo é o do próprio node, comparamos com o valor
    # de cada filho (obtido recursivamente) para ver qual é maior
    best_so_far = tree['value']

    for child in tree['children']:
        best_child_value = tree_max(child)  # maior valor na árvore filha

        if best_child_value > best_so_far:
            best_so_far = best_child_value

    return best_so_far


def binary_tree_max(tree):
    """
    Finds the maximum value in a proper binary tree.

    Args:
        tree: dict representation of a proper binary tree where nodes have numerical values

    Returns:
        maximum node value of tree
    """
    # a função de árvore genérica funciona para binárias, então só chamar essa função
    return tree_max(tree)
