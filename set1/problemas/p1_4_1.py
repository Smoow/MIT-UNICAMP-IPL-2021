poly = [-8, 7, 0, 4]
out = []

if (len(poly) == 0):
    out = None
else:
    for i in range(len(poly)):
        out.append(int(i*poly[i]))
    del out[0]

print(out)