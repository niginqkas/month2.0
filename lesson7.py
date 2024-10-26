import sqlite3

conn = sqlite3.connect("hw.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL,
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
''')
conn.commit()


def add_products():
    products = [
        ("Мыло детское", 50.0, 10),
        ("Шампунь", 120.0, 20),
        ("Зубная паста", 75.0, 5),
        ("Мыло хозяйственное", 40.0, 15),
        ("Кондиционер для волос", 150.0, 8),
        ("Лосьон для тела", 90.0, 12),
        ("Крем для рук", 55.0, 25),
        ("Пена для ванны", 130.0, 6),
        ("Гель для душа", 110.0, 9),
        ("Туалетное мыло", 60.0, 18),
        ("Зубная щетка", 80.0, 30),
        ("Крем для лица", 160.0, 7),
        ("Маска для лица", 70.0, 14),
        ("Крем после бритья", 85.0, 11),
        ("Дезодорант", 100.0, 20)
    ]
    cursor.executemany('''
        INSERT INTO products (product_title, price, quantity)
        VALUES (?, ?, ?)
    ''', products)
    conn.commit()


def update_quantity(product_id, new_quantity):
    cursor.execute('''
        UPDATE products
        SET quantity = ?
        WHERE id = ?
    ''', (new_quantity, product_id))
    conn.commit()


def update_price(product_id, new_price):
    cursor.execute('''
        UPDATE products
        SET price = ?
        WHERE id = ?
    ''', (new_price, product_id))
    conn.commit()


def delete_product(product_id):
    cursor.execute('''
        DELETE FROM products
        WHERE id = ?
    ''', (product_id,))
    conn.commit()


def show_all_products():
    cursor.execute('''
        SELECT * FROM products
    ''')
    products = cursor.fetchall()
    for product in products:
        print(product)


def filter_products(price_limit=100.0, quantity_limit=5):
    cursor.execute('''
        SELECT * FROM products
        WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    products = cursor.fetchall()
    for product in products:
        print(product)


def search_product_by_name(keyword):
    cursor.execute('''
        SELECT * FROM products
        WHERE product_title LIKE ?
    ''', ('%' + keyword + '%',))
    products = cursor.fetchall()
    for product in products:
        print(product)


def test_functions():
    add_products()
    print("Все товары:")
    show_all_products()

    print("\nИзменяем количество товара с id=1 на 50:")
    update_quantity(1, 50)
    show_all_products()

    print("\nИзменяем цену товара с id=2 на 99.99:")
    update_price(2, 99.99)
    show_all_products()

    print("\nУдаляем товар с id=3:")
    delete_product(3)
    show_all_products()

    print("\nТовары, дешевле 100 сомов и количество больше 5:")
    filter_products()

    print("\nПоиск товаров с названием 'мыло':")
    search_product_by_name("мыло")


test_functions()

conn.close()
