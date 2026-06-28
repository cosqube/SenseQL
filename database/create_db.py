import sqlite3
import os

# Optional: Delete the old database during development
db_path = 'database/company.db'
if os.path.exists(db_path):
    os.remove(db_path)

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Table 1: Customers
cursor.execute('''
    CREATE TABLE Customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        city TEXT,
        signup_date DATE
    )
''')

# Table 2: Categories
cursor.execute('''
    CREATE TABLE Categories (
        category_id INTEGER PRIMARY KEY,
        category_name TEXT
    )
''')

# Table 3: Products
cursor.execute('''
    CREATE TABLE Products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        category_id INTEGER,
        price REAL,
        stock INTEGER,
        FOREIGN KEY (category_id) REFERENCES Categories(category_id)
    )
''')

# Table 4: Orders
cursor.execute('''
    CREATE TABLE Orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date DATE,
        total_amount REAL,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
''')

# Table 5: Order_Items
cursor.execute('''
    CREATE TABLE Order_Items (
        order_item_id INTEGER PRIMARY KEY,
        order_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        unit_price REAL,
        FOREIGN KEY (order_id) REFERENCES Orders(order_id),
        FOREIGN KEY (product_id) REFERENCES Products(product_id)
    )
''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()

# Print success message
print("Database created successfully!")
