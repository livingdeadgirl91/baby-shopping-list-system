
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_id):
        self.items = [i for i in self.items if i.item_id != item_id]

    def calculate_total(self):
        return sum(item.price for item in self.items)
