from collections import namedtuple

Item = namedtuple('Item', ['name', 'price'])


class VendingMachine(object):
    def __init__(self):
        super(VendingMachine, self).__init__()
        self.inventory = dict()

    def add_to_inventory(self, item_name, price):
        self.inventory[item_name] = Item(item_name, price)

    def sell_item(self, item_name, amount):
        item = self.inventory.get(item_name)
        if item and amount >= item.price:
            return item

    def get_item_price(self, item):
        return self.inventory.get(item).price

