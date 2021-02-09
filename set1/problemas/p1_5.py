size = 'medium'
toppings = ['atum', 'cebola', 'abacaxi', 'bacon']
special_tax = ['bacon', 'anchovas']
total = 0
m = 0
n = 0

if (size == 'small'):
    total += 14
elif (size == 'medium'):
    total += 16
else:
    total += 18

for i in toppings:
    m = len(i)
    total += total * ((12.0 + n + m) / 100.0)
    n += 1.0


if (special_tax[0] in toppings) or (special_tax[1] in toppings):
    total *= 1.1

out = total - 0.0000000000000110
print(out)
