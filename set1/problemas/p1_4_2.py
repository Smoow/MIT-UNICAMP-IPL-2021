poly = [-8.0, 7.0, 0.0, 4.0]
const = poly[0]
out = [int(const)]

for i in range(0, len(poly)):
    out.append(poly[i]/(i+1))

print(out)
