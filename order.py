
from payment import Payment

class Order:
    def __init__(self, cart, order_id):
        self.order_id = order_id
        self.cart = cart
        self.status = "Pending"
        self.payment = Payment()

    def confirm(self):
        total = self.cart.calculate_total()
        if self.payment.process(total) == "Success":
            self.status = "Confirmed"
            print(f"Order {self.order_id} confirmed.")
