
from item import Item

class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def search(self, keyword):
        return [item for item in self.items if keyword.lower() in item.name.lower()]
