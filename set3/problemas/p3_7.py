def hailstone_sequence(a_0):
    out = []

    out.append(a_0)
    if a_0 == 1:
        return out

    while a_0 > 1:
        if a_0 % 2 == 0:
            a_0 /= 2
            out.append(a_0)
        else:
            a_0 = 3*a_0+1
            out.append(a_0)

    return out
