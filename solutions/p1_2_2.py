numbers = [2, 7, 3, 9, 13, 12, -4]

if len(numbers) == 0:
    out = None
else:
    total_prod = 1  # representa produto de todos os elementos
    for elem in numbers:
        total_prod *= elem
    out = total_prod ** (1 / len(numbers))
