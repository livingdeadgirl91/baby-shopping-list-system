
class Payment:
    def __init__(self):
        self.status = "Pending"

    def process(self, amount):
        print(f"Processing payment of ${amount:.2f}")
        self.status = "Success"
        return self.status
