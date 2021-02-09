a = 2
b = 4
c = 6

if a == 0:
    out = -c/b
else:
    x = ((b ** 2) - (4 * a * c)) ** 0.5
    x1 = (-b + x) / (2 * a)
    x2 = (-b - x) / (2 * a)

    out = x1, x2

print(out)
