import sqlite3

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as error:
        print(error)
    return connection

sql_to_create_employees_table = '''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(150) NOT NULL

)'''
db_name = '''practical_assigment.db'''
my_connection = create_connection(db_name)
if my_connection is not None:
    print("Connected to database")
    my_connection.close()



    onn = sqlite3.connect('store_database.db')
    cursor = conn.cursor()


    def display_stores():
        cursor.execute("SELECT store_id, title FROM store")
        stores = cursor.fetchall()
        print(
            "Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
        for store in stores:
            print(f"{store[0]}. {store[1]}")
        return [store[0] for store in stores]


    def display_products(store_id):
        query = """
        SELECT products.title, categories.title, products.unit_price, products.stock_quantity
        FROM products
        JOIN categories ON products.category_code = categories.code
        WHERE products.store_id = ?
        """
        cursor.execute(query, (store_id,))
        products = cursor.fetchall()

        if products:
            for product in products:
                print(f"\nНазвание продукта: {product[0]}")
                print(f"Категория: {product[1]}")
                print(f"Цена: {product[2]}")
                print(f"Количество на складе: {product[3]}")
        else:
            print("В выбранном магазине нет доступных продуктов.")


    def main():
        while True:
            store_ids = display_stores()
            store_id = input("Введите id магазина для отображения продуктов (или 0 для выхода): ")

            if store_id == '0':
                print("Программа завершена.")
                break
            elif store_id.isdigit() and int(store_id) in store_ids:
                display_products(int(store_id))
            else:
                print("Некорректный id магазина. Пожалуйста, попробуйте снова.")


    if __name__ == "__main__":
        try:
            main()
        finally:

            conn.close()