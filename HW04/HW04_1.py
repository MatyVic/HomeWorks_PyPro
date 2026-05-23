import csv
from generate_files import gen_csv

gen_csv()


class Product:
    def __init__(self, name, price, prod_category, quantity):
        self.name = name
        self.price = price
        self.category = prod_category
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def update_price(self, new_price):
        self.price = new_price


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def create_new_order(self):
        order = Order()
        self.orders.append(order)
        return order


class Order:
    def __init__(self):
        self.product_list = []
        self.final_price = 0

    def add_product_to_list(self, product, quantity):
        if product.quantity >= quantity:
            self.product_list.append((product, quantity))
        else:
            raise ValueError(f"There is no such quantity of {product.name}")

    def check_product_order(self):
        cart_price = 0
        for item, qty in self.product_list:
            cart_price += qty * item.price
        self.final_price = cart_price
        return self.final_price


# Завантаження попередніх даних
products = []
with open("products.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = Product(
            name=row["name"],
            price=float(row["price"]),
            prod_category=row["category"],
            quantity=int(row["quantity"])
        )
        products.append(product)

customers = []
with open("customers.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        customer = Customer(name=row["customer_name"], email=row["email"])
        customers.append(customer)


with open("orders.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        customer = next(c for c in customers if c.name == row["customer"])
        product = next(p for p in products if p.name == row["product"])
        order = customer.create_new_order()
        order.add_product_to_list(product, int(row["quantity"]))
        order.check_product_order()

print("\n---Початкові замовлення---")
for customer in customers:
    print(f"Клієнт: {customer.name}, Email: {customer.email}")
    for order in customer.orders:
        print("  Замовлення:")
        for product, qty in order.product_list:
            print(f"    {product.name} x {qty} Ціна: {product.price}")
        print(f"  Загальна сума: {order.final_price} грн")
        print('-' * 50)


print("\n--- Оновлення ціни ---")
lego = next(p for p in products if p.name == "LEGO")
print(f"Стара ціна LEGO: {lego.price} грн")
lego.update_price(1500)
print(f"Нова ціна LEGO: {lego.price} грн")


print("\n--- Нове замовлення ---")
ivan = next(c for c in customers if c.name == "Іван")
new_order = ivan.create_new_order()
new_order.add_product_to_list(lego, 1)
new_order.add_product_to_list(next(p for p in products if p.name == "Книга"), 2)
new_order.check_product_order()


print(f"Клієнт: {ivan.name} створив нове замовлення:")
for product, qty in new_order.product_list:
    print(f"    {product.name} x {qty}")
print(f"  Загальна сума: {new_order.final_price} грн")
