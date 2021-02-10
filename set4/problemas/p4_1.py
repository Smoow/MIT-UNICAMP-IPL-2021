def warehouse_process(wares: dict, trans: tuple):
    act, order, amount = trans

    if (act == "receive"):
        if order in wares:
            wares[order] += amount
        else:
            wares[order] = amount
    elif (act == "ship"):
        if wares[order] < amount:
            wares[order] = 0
            print("not enough")
        else:
            wares[order] -= amount

    return


class Warehouse:
    def __init__(self):
        self.wares = {}

    def process(self, trans):
        warehouse_process(self.wares, trans)

    def lookup(self, product):
        if product in self.wares:
            return self.wares[product]
        else:
            return 0
