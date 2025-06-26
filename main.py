
from customer import Customer
from catalog import Catalog
from item import Item

# Set up catalog
catalog = Catalog()
catalog.add_item(Item(1, "Baby Diapers", 19.99, 100))
catalog.add_item(Item(2, "Baby Wipes", 5.99, 200))

# Simulate a customer shopping experience
customer = Customer("Alice", "alice@example.com", "securepass")
customer.register()
customer.login()

# Browse and add to cart
items = catalog.search("baby")
for item in items:
    print(item.get_details())
    customer.shopping_cart.add_item(item)

# Place order
customer.place_order()
