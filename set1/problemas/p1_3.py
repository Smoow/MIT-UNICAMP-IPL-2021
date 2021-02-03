dividend = 31
divisor = 5
tmp = divisor
rest = 0
counter = 0

while (tmp < dividend):
    tmp += divisor
    counter += 1

rest = dividend - (divisor * counter)

out = (counter, rest)
print(out)
