# Consegui a primeira parte... preciso adaptar para funcionar para
# qualquer tree que tenha mais childrens
def binary_tree_max(tree):
    x = tree.get('children')
    for i in range(len(x)):
        values.append(x[i].get('value'))
        y = x[i].get('children')
        if (len(y) > 0): 
            for j in range(len(y)):
                values.append(y[j].get('value'))
                z = y[j].get('children')
                if (len(z) > 0):
                    for k in range(len(z)):
                        values.append(z[k].get('value'))

    return values

tree = {'value': 13, 
 'children': [{'value': 7, 'children': []},
              {'value': 8,
               'children': [{'value': 99, 'children': []},
                            {'value': 16,
                             'children': [{'value': 77, 'children': []}]},
                            {'value': 42, 'children': []}]}]}


values = [tree.get('value')]
print(binary_tree_max(tree))
values.sort()
print(values)
