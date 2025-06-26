
class Item:
    def __init__(self, item_id, name, price, stock):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.stock = stock

    def get_details(self):
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"
