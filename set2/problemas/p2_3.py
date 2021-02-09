def ndoors(doors):
    doors_locked = [i for i in range(1, doors+1)]
    doors_unlocked = []

    for i in range(1, doors+1):
        for j in range(1, doors+1):
            if (j % i == 0):
                if j in doors_locked:
                    doors_locked.remove(j)
                    doors_unlocked.append(j)
                else:
                    doors_locked.append(j)
                    doors_unlocked.remove(j)

    return doors_unlocked


print(ndoors(1000))
