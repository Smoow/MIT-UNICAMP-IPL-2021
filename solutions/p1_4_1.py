poly = [-8, 9, 32, 0, -3, 2]

# final tem um elemento a menos (derivada de constante = zero)
out = [0] * (len(poly) - 1)

for index in range(1, len(poly)):
    out[index - 1] = poly[index] * index
