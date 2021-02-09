poly = [-8, 9, 32, 0, -3, 2]
const = 24

# final tem um elemento a mais (constante introduzida)
out = [0] * (len(poly) + 1)

out[0] = const  # constante = termo independente
for index in range(1, len(poly) + 1):
    out[index] = poly[index - 1] / index
