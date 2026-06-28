import sqlite3
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker with Indian locale
fake = Faker('en_IN')

# Database connection
conn = sqlite3.connect('database/company.db')
cursor = conn.cursor()

# ============================================
# Step 1: Insert Categories (manually)
# ============================================
categories = [
    'Electronics',
    'Clothing',
    'Books',
    'Home & Kitchen',
    'Sports',
    'Beauty',
    'Toys',
    'Groceries'
]

for category in categories:
    cursor.execute('INSERT INTO Categories (category_name) VALUES (?)', (category,))

print(f"✓ Inserted {len(categories)} categories")

# ============================================
# Step 2: Insert Customers (200 using Faker)
# ============================================
indian_cities = [
    'Delhi', 'Mumbai', 'Bengaluru', 'Hyderabad',
    'Chennai', 'Pune', 'Kolkata', 'Jaipur',
    'Lucknow', 'Chandigarh', 'Indore', 'Bhopal'
]

for i in range(200):
    name = fake.name()
    email = fake.email()
    city = random.choice(indian_cities)
    # Signup date within last 2 years
    signup_date = fake.date_between(start_date='-2y')
    
    cursor.execute('''
        INSERT INTO Customers (name, email, city, signup_date)
        VALUES (?, ?, ?, ?)
    ''', (name, email, city, signup_date))

print("✓ Inserted 200 customers")

# ============================================
# Step 3: Insert Products (100 curated)
# ============================================
products_data = {
    'Electronics': [
        ('Laptop', 75000, 50),
        ('Smartphone', 35000, 120),
        ('Keyboard', 5000, 200),
        ('Mouse', 2000, 300),
        ('Monitor', 15000, 80),
        ('Earbuds', 4000, 150),
        ('Smartwatch', 12000, 60),
        ('USB Cable', 500, 500),
        ('Phone Charger', 1500, 300),
        ('Screen Protector', 300, 1000),
        ('Phone Case', 800, 400),
        ('Laptop Stand', 3000, 100),
        ('External Hard Drive', 8000, 90),
        ('SSD 256GB', 5000, 120),
    ],
    'Clothing': [
        ('T-Shirt', 500, 300),
        ('Jeans', 2000, 200),
        ('Shirt', 1500, 250),
        ('Trousers', 2500, 180),
        ('Jacket', 5000, 100),
        ('Dress', 3000, 150),
        ('Skirt', 1800, 120),
        ('Shorts', 1200, 200),
        ('Sweater', 2000, 150),
        ('Hoodie', 2500, 180),
        ('Socks', 300, 500),
        ('Underwear Set', 800, 300),
        ('Saree', 4000, 80),
        ('Kurta', 1500, 200),
    ],
    'Books': [
        ('Python Programming', 800, 100),
        ('Data Science Handbook', 1500, 80),
        ('Web Development Guide', 900, 90),
        ('Machine Learning Basics', 1200, 70),
        ('SQL Mastery', 700, 120),
        ('Fiction Novel', 400, 200),
        ('Self-Help Book', 500, 150),
        ('Biography', 600, 100),
        ('History Book', 700, 80),
        ('Travel Guide', 550, 90),
        ('Cooking Book', 650, 110),
        ('Art & Design', 1100, 60),
        ('Business Strategy', 950, 75),
        ('Philosophy', 800, 85),
    ],
    'Home & Kitchen': [
        ('Coffee Maker', 5000, 70),
        ('Blender', 3000, 100),
        ('Microwave', 12000, 50),
        ('Oven', 15000, 30),
        ('Toaster', 2000, 80),
        ('Bed Sheet Set', 2000, 150),
        ('Pillow', 1500, 200),
        ('Blanket', 2500, 120),
        ('Curtains', 3000, 100),
        ('Door Mat', 500, 300),
        ('Kitchen Knife Set', 2000, 90),
        ('Cookware Set', 8000, 50),
        ('Dining Table', 20000, 20),
        ('Chair', 5000, 60),
    ],
    'Sports': [
        ('Football', 1000, 80),
        ('Cricket Bat', 3000, 60),
        ('Yoga Mat', 1500, 150),
        ('Dumbbells Set', 5000, 100),
        ('Running Shoes', 4000, 120),
        ('Basketball', 1500, 70),
        ('Tennis Racket', 4000, 50),
        ('Badminton Set', 2000, 80),
        ('Swimming Goggles', 1000, 150),
        ('Cycling Helmet', 2000, 90),
        ('Water Bottle', 800, 300),
        ('Gym Bag', 1500, 120),
        ('Resistance Bands', 1000, 200),
        ('Jump Rope', 500, 250),
    ],
    'Beauty': [
        ('Face Wash', 400, 300),
        ('Moisturizer', 800, 250),
        ('Sunscreen', 600, 280),
        ('Shampoo', 500, 300),
        ('Conditioner', 500, 250),
        ('Lipstick', 500, 200),
        ('Foundation', 800, 180),
        ('Mascara', 600, 150),
        ('Face Mask', 300, 400),
        ('Body Lotion', 700, 250),
        ('Nail Polish', 350, 300),
        ('Perfume', 2000, 100),
        ('Deodorant', 400, 250),
        ('Hair Oil', 300, 400),
    ],
    'Toys': [
        ('LEGO Set', 3000, 60),
        ('Action Figure', 1500, 100),
        ('Puzzle', 500, 150),
        ('Board Game', 1000, 80),
        ('Doll', 2000, 90),
        ('Remote Car', 3000, 50),
        ('Building Blocks', 1500, 120),
        ('Bicycle', 8000, 40),
        ('Skateboard', 3500, 50),
        ('Scooter', 5000, 60),
        ('Balls Set', 800, 150),
        ('Coloring Book', 200, 300),
        ('Toy Train', 2500, 70),
        ('Video Game', 4000, 80),
    ],
    'Groceries': [
        ('Rice Bag', 500, 500),
        ('Flour', 300, 400),
        ('Oil Can', 800, 300),
        ('Sugar', 400, 350),
        ('Salt', 150, 600),
        ('Spices Pack', 500, 200),
        ('Pasta', 200, 400),
        ('Cereal Box', 300, 300),
        ('Milk Powder', 600, 250),
        ('Honey', 800, 150),
        ('Peanut Butter', 500, 200),
        ('Tea Leaves', 400, 250),
        ('Coffee Powder', 600, 200),
        ('Chocolate Spread', 400, 180),
    ]
}

product_count = 0
for category_name, products in products_data.items():
    # Get category ID
    cursor.execute('SELECT category_id FROM Categories WHERE category_name = ?', (category_name,))
    category_id = cursor.fetchone()[0]
    
    for product_name, price, stock in products:
        cursor.execute('''
            INSERT INTO Products (product_name, category_id, price, stock)
            VALUES (?, ?, ?, ?)
        ''', (product_name, category_id, price, stock))
        product_count += 1

print(f"✓ Inserted {product_count} products")

# ============================================
# Step 4: Insert Orders (800) and Order Items (2000-3000)
# ============================================
# Get all customer and product IDs
cursor.execute('SELECT customer_id FROM Customers')
customer_ids = [row[0] for row in cursor.fetchall()]

cursor.execute('SELECT product_id, price FROM Products')
products_list = cursor.fetchall()  # (product_id, price)

order_count = 0
order_item_count = 0
two_years_ago = datetime.now() - timedelta(days=730)

for i in range(800):
    customer_id = random.choice(customer_ids)
    order_date = fake.date_between(start_date=two_years_ago)
    
    # Insert order with placeholder total (will be updated later)
    cursor.execute('''
        INSERT INTO Orders (customer_id, order_date, total_amount)
        VALUES (?, ?, ?)
    ''', (customer_id, order_date, 0))
    
    order_id = cursor.lastrowid
    order_count += 1
    
    # Generate 1-5 order items
    num_items = random.randint(1, 5)
    total_amount = 0
    
    for _ in range(num_items):
        product_id, price = random.choice(products_list)
        quantity = random.randint(1, 5)
        unit_price = price
        
        cursor.execute('''
            INSERT INTO Order_Items (order_id, product_id, quantity, unit_price)
            VALUES (?, ?, ?, ?)
        ''', (order_id, product_id, quantity, unit_price))
        
        total_amount += quantity * unit_price
        order_item_count += 1
    
    # Update order total amount
    cursor.execute('UPDATE Orders SET total_amount = ? WHERE order_id = ?', (total_amount, order_id))

print(f"✓ Inserted {order_count} orders with {order_item_count} order items")

# ============================================
# Commit and Close
# ============================================
conn.commit()
conn.close()

print("\n✅ Database populated successfully!")
print(f"   - Categories: 8")
print(f"   - Customers: 200")
print(f"   - Products: {product_count}")
print(f"   - Orders: {order_count}")
print(f"   - Order Items: {order_item_count}")
