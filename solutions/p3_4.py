def lend_money(debts, person, amount):
    """
    Adds log of amount money being lent to person in registry debts

    Args:
        debts: dict mapping friend name to list of transactions
        person: person borrowing money
        amount: amount of money borrowed

    Returns:
        None
    """
    if person in debts:
        # apenas adiciona mais um empréstimo
        debts[person].append(amount)
    else:
        # adiciona a pessoa e o valor do primeiro empréstimo
        debts[person] = [amount]


def amount_owed_by(debts, person):
    """
    Retrieves amount owed by friend person in registry debts

    Args:
        debts: dict mapping friend name to list of transactions
        person: friend whose debt to check

    Returns:
        Total amount owed by person (0 if not in debts)
    """
    if person in debts:
        # retorna a soma de todos os valores na lista da pessoa
        return sum(debts[person])
    else:
        # pessoa não no dicionário: nada devido
        return 0


def total_amount_owed(debts):
    """
    Retrieves amount owed by all friends together in registry debts

    Args:
        debts: dict mapping friend name to list of transactions

    Returns:
        Total amount owed by all friends
    """
    total = 0

    for person in debts:
        # soma os valores devidos para cada pessoa para obter um total
        total += sum(debts[person])

    return total
