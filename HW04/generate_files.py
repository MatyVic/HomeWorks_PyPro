import csv

print(ff)
def gen_csv():
    products = [
        ["name", "category", "price", "quantity"],
        ["Ведмедик", "м'яка іграшка", 300, 10],
        ["LEGO", "конструктор", 1200, 5],
        ["М'яч", "спорт", 150, 20],
        ["Книга", "література", 200, 15],
    ]

    with open("products.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(products)

    customers = [
        ["customer_name", "email"],  # заголовки колонок
        ["Іван", "ivan@example.com"],
        ["Марія", "maria@example.com"],
        ["Олег", "oleg@example.com"],
    ]

    with open("customers.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(customers)

    orders = [
        ["customer", "product", "quantity"],
        ["Іван", "Ведмедик", 2],
        ["Іван", "LEGO", 1],
        ["Марія", "Книга", 3],
        ["Олег", "М'яч", 5],
    ]

    with open("orders.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(orders)
