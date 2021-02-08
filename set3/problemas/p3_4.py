def lend_money(debts, person, amount):
    flag = 0
    for key in debts:
        if key == person:
            flag = 1
            debts[person].append(amount)

    if (flag == 0): debts[person] = [amount]
        
    return None


def amount_owed_by(debts, person):
    flag = 0
    s_v = 0
    for key in debts:
        if key == person:
            flag = 1
            for values in debts[person]:
                s_v += values
            return s_v

    if (flag == 0): return 0


def total_amount_owed(debts):
    total = 0
    for keys in debts:
        for values in debts[keys]:
            total += values

    return total

debts = {}
