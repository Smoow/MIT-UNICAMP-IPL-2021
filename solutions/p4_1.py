def warehouse_process(wares, transaction):
    """
    Processes a transaction in a given warehouse represented by registry wares

    Args:
        wares: dict containing total information about warehouse
        transaction: tuple of form (action, product, amount)
            action can be 'receive' or 'ship'

    Returns:
        None (prints "not enough" for shipping transactions with not enough material)
    """
    action, product, amount = transaction

    if action == 'receive':
        if product in wares:  # já presente, apenas adiciona amount
            wares[product] += amount
        else:  # cria entrada, valor inicial zero, adiciona amount
            wares[product] = amount

    elif action == 'ship':
        if product not in wares or wares[product] < amount:
            # não há material suficiente: imprimir mensagem de erro e zerar valor
            print('not enough')
            wares[product] = 0
        else:
            # retirar amount da quantidade existente
            wares[product] -= amount


class Warehouse:
    def __init__(self):
        """Initializes empty dictionary as internal representation"""
        self._stock = {}

    def process(self, transaction):
        """Just use function defined above for processing"""
        warehouse_process(self._stock, transaction)

    def lookup(self, pdt):
        """Checks _stock of given pdt; 0 if not present"""
        if pdt in self._stock:
            return self._stock[pdt]

        return 0
