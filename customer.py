
from shopping_cart import ShoppingCart
from order import Order

class Customer:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.shopping_cart = ShoppingCart()
        self.orders = []

    def register(self):
        print(f"Registered user: {self.name}")

    def login(self):
        print(f"Logged in as: {self.name}")

    def place_order(self):
        order = Order(self.shopping_cart, len(self.orders) + 1)
        order.confirm()
        self.orders.append(order)
