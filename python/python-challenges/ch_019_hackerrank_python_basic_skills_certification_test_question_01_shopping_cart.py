class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart(Item):
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total(self):
        total_price = 0
        if self.items:
            for item in self.items:
                total_price += item.price
        return total_price

    def __len__(self):
        return len(self.items)
