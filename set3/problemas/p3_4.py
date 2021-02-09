def lend_money(debts, person, amount):
    if person in debts:
        debts[person].append(amount)
    else:
        debts[person] = [amount]

    return None


def amount_owed_by(debts, person):
    s_v = 0
    if person in debts:
        for values in debts[person]:
            s_v += values
        return s_v
    else:
        return 0


def total_amount_owed(debts):
    total = 0
    for keys in debts:
        for values in debts[keys]:
            total += values

    return total
