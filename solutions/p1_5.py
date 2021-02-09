size = 'small'
toppings = ['bacon', 'atum', 'calabresa', 'amendoim', 'anchovas', 'abacaxi']

if size == 'small':
    cost = 14
elif size == 'medium':
    cost = 16
elif size == 'large':
    cost = 18
else:
    cost = float("inf")

extra_fee = False  # armazena se a pizza tem bacon ou anchovas

for n, topping in enumerate(toppings):
    cost *= 1 + (12 + n + len(topping)) / 100

    if topping == 'bacon' or topping == 'anchovas':
        extra_fee = True

# o if/else abaixo pode ser escrito como:
# out = 1.1 * cost if extra_fee else cost
if extra_fee:
    out = 1.1 * cost
else:
    out = cost
