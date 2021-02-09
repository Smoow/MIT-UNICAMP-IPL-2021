a = 1
b = 2
c = 3

if a == 0:
    # equação de primeiro grau
    out = - c / b
else:
    # equação de segundo grau
    out = (-b + (b ** 2 - 4*a*c) ** 0.5) / (2*a), (-b - (b ** 2 - 4*a*c) ** 0.5) / (2*a)
