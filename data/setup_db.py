"""
E-Commerce Database Setup
=========================
Tabele: categories, products, customers, orders, order_items
Rânduri: ~500+ înregistrări realiste

Rulare:
    pip install pandas sqlalchemy faker
    python setup_ecommerce_db.py

Conexiune DBeaver:
    New Connection → SQLite → selectează ecommerce.db
"""

import pandas as pd
import random
from datetime import datetime, timedelta
from sqlalchemy import create_engine
import os

random.seed(42)

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ecommerce.db")
engine = create_engine(f"sqlite:///{db_path}")

# ─── 1. CATEGORIES ────────────────────────────────────────────────────────────
categories_data = [
    (1,  "Laptops",          "Laptop-uri si notebook-uri"),
    (2,  "Smartphones",      "Telefoane mobile si accesorii"),
    (3,  "Tablets",          "Tablete si e-readere"),
    (4,  "Audio",            "Casti, boxe, sisteme audio"),
    (5,  "Monitors",         "Monitoare si display-uri"),
    (6,  "Peripherals",      "Tastatura, mouse, hub-uri"),
    (7,  "Storage",          "SSD, HDD, stick-uri USB"),
    (8,  "Networking",       "Router, switch, accesorii retea"),
    (9,  "Gaming",           "Echipamente gaming"),
    (10, "Office",           "Imprimante, scanere, biroticare"),
]

categories = pd.DataFrame(categories_data, columns=["category_id", "name", "description"])

# ─── 2. PRODUCTS ──────────────────────────────────────────────────────────────
products_data = [
    # Laptops
    (1,  "MacBook Pro 14",        1, 2499.99, 1899.99, 45),
    (2,  "MacBook Air M2",        1, 1499.99, 1099.99, 80),
    (3,  "Dell XPS 15",           1, 1899.99, 1399.99, 35),
    (4,  "Lenovo ThinkPad X1",    1, 1699.99, 1299.99, 50),
    (5,  "HP Spectre x360",       1, 1599.99, 1199.99, 40),
    (6,  "Asus ZenBook 14",       1,  999.99,  749.99, 60),
    (7,  "Acer Swift 3",          1,  699.99,  499.99, 75),
    # Smartphones
    (8,  "iPhone 15 Pro",         2, 1299.99,  999.99, 100),
    (9,  "iPhone 15",             2,  999.99,  749.99, 120),
    (10, "Samsung Galaxy S24",    2, 1199.99,  899.99, 90),
    (11, "Samsung Galaxy A54",    2,  499.99,  349.99, 150),
    (12, "Google Pixel 8",        2,  799.99,  599.99, 70),
    (13, "OnePlus 12",            2,  699.99,  499.99, 55),
    # Tablets
    (14, "iPad Pro 12.9",         3, 1199.99,  899.99, 40),
    (15, "iPad Air",              3,  799.99,  599.99, 60),
    (16, "Samsung Galaxy Tab S9", 3,  899.99,  649.99, 45),
    (17, "Kindle Paperwhite",     3,  149.99,   99.99, 200),
    # Audio
    (18, "AirPods Pro",           4,  299.99,  219.99, 150),
    (19, "Sony WH-1000XM5",       4,  399.99,  279.99, 80),
    (20, "Bose QC45",             4,  349.99,  249.99, 65),
    (21, "JBL Charge 5",          4,  199.99,  139.99, 120),
    (22, "Sonos One",             4,  249.99,  179.99, 50),
    # Monitors
    (23, "LG 27UK850",            5,  699.99,  499.99, 30),
    (24, "Dell UltraSharp 27",    5,  799.99,  579.99, 25),
    (25, "Samsung Odyssey G7",    5,  599.99,  429.99, 35),
    (26, "BenQ PD2700U",          5,  649.99,  469.99, 20),
    # Peripherals
    (27, "Logitech MX Master 3",  6,  109.99,   74.99, 200),
    (28, "Apple Magic Keyboard",  6,  129.99,   89.99, 150),
    (29, "Keychron K2",           6,   99.99,   69.99, 180),
    (30, "Logitech MX Keys",      6,  119.99,   84.99, 160),
    (31, "Razer DeathAdder V3",   6,   79.99,   54.99, 220),
    # Storage
    (32, "Samsung T7 1TB SSD",    7,  119.99,   84.99, 300),
    (33, "WD My Passport 2TB",    7,   89.99,   59.99, 250),
    (34, "SanDisk Extreme 512GB", 7,   79.99,   54.99, 400),
    (35, "Seagate 4TB HDD",       7,   99.99,   69.99, 180),
    # Networking
    (36, "TP-Link Archer AX73",   8,  199.99,  139.99, 90),
    (37, "Asus RT-AX88U",         8,  299.99,  219.99, 60),
    (38, "Netgear Nighthawk",     8,  249.99,  179.99, 75),
    # Gaming
    (39, "Razer Blade 15",        9, 2299.99, 1749.99, 25),
    (40, "ASUS ROG Strix G15",    9, 1499.99, 1099.99, 40),
    (41, "Xbox Controller",       9,   69.99,   49.99, 300),
    (42, "PS5 DualSense",         9,   79.99,   54.99, 250),
    (43, "SteelSeries Arctis 7",  9,  149.99,  104.99, 120),
    # Office
    (44, "HP LaserJet Pro",      10,  399.99,  279.99, 40),
    (45, "Canon PIXMA G7020",    10,  299.99,  209.99, 55),
    (46, "Brother HL-L2350DW",   10,  199.99,  139.99, 70),
    (47, "Epson EcoTank ET-4850",10,  449.99,  314.99, 35),
    (48, "Webcam Logitech C920", 6,    89.99,   62.99, 200),
    (49, "USB-C Hub 7-in-1",     6,    49.99,   34.99, 350),
    (50, "Monitor Stand Adjustable", 5, 79.99,  54.99, 100),
]

products = pd.DataFrame(products_data, columns=[
    "product_id", "name", "category_id", "price", "cost", "stock_qty"
])

# ─── 3. CUSTOMERS ─────────────────────────────────────────────────────────────
first_names = [
    "Marco", "Giulia", "Luca", "Sofia", "Alessandro", "Martina", "Francesco",
    "Elena", "Andrea", "Chiara", "Matteo", "Sara", "Lorenzo", "Laura",
    "Davide", "Anna", "Simone", "Federica", "Riccardo", "Valentina",
    "Emanuele", "Claudia", "Stefano", "Monica", "Paolo", "Roberta",
    "Giovanni", "Alessia", "Roberto", "Silvia"
]

last_names = [
    "Rossi", "Ferrari", "Russo", "Bianchi", "Romano", "Gallo", "Costa",
    "Fontana", "Conti", "Esposito", "Ricci", "Bruno", "De Luca", "Moretti",
    "Barbieri", "Lombardi", "Marino", "Greco", "Giordano", "Colombo",
    "Mancini", "Longo", "Leone", "Gentile", "Pellegrini", "Marini",
    "Martinelli", "Ferrara", "Caruso", "Fiore"
]

cities = [
    "Milano", "Roma", "Torino", "Napoli", "Bologna", "Firenze",
    "Venezia", "Palermo", "Genova", "Bari", "Catania", "Verona",
    "Padova", "Trieste", "Brescia", "Parma", "Modena", "Reggio Emilia",
    "Perugia", "Livorno"
]

regions = {
    "Milano": "Lombardia", "Torino": "Piemonte", "Genova": "Liguria",
    "Venezia": "Veneto", "Padova": "Veneto", "Verona": "Veneto",
    "Trieste": "Friuli", "Bologna": "Emilia-Romagna", "Parma": "Emilia-Romagna",
    "Modena": "Emilia-Romagna", "Reggio Emilia": "Emilia-Romagna",
    "Firenze": "Toscana", "Livorno": "Toscana", "Perugia": "Umbria",
    "Roma": "Lazio", "Napoli": "Campania", "Bari": "Puglia",
    "Palermo": "Sicilia", "Catania": "Sicilia", "Brescia": "Lombardia"
}

customers_list = []
for i in range(1, 31):
    first = first_names[i-1]
    last = last_names[i-1]
    city = random.choice(cities)
    
    # signup date intre 2022-01-01 si 2023-12-31
    signup = datetime(2022, 1, 1) + timedelta(days=random.randint(0, 730))
    
    # segment bazat pe customer_id
    if i <= 5:
        segment = "VIP"
    elif i <= 15:
        segment = "Regular"
    else:
        segment = "New"
    
    customers_list.append({
        "customer_id": i,
        "first_name": first,
        "last_name": last,
        "email": f"{first.lower()}.{last.lower().replace(' ', '')}@email.it",
        "city": city,
        "region": regions.get(city, "Italia"),
        "signup_date": signup.strftime("%Y-%m-%d"),
        "segment": segment
    })

customers = pd.DataFrame(customers_list)

# ─── 4. ORDERS ────────────────────────────────────────────────────────────────
statuses = ["completed", "completed", "completed", "completed", "shipped", "processing", "cancelled"]
channels = ["web", "web", "web", "mobile", "mobile", "email"]

orders_list = []
order_id = 1001

for customer_id in range(1, 31):
    # VIP: 8-12 comenzi, Regular: 4-7, New: 1-3
    if customer_id <= 5:
        n_orders = random.randint(8, 12)
    elif customer_id <= 15:
        n_orders = random.randint(4, 7)
    else:
        n_orders = random.randint(1, 3)
    
    # Prima comanda dupa signup
    customer_signup = datetime.strptime(
        customers_list[customer_id-1]["signup_date"], "%Y-%m-%d"
    )
    
    order_dates = sorted([
        customer_signup + timedelta(days=random.randint(1, 600))
        for _ in range(n_orders)
    ])
    
    for order_date in order_dates:
        if order_date > datetime(2024, 12, 31):
            continue
            
        discount_pct = random.choice([0, 0, 0, 5, 10, 15, 20])
        
        orders_list.append({
            "order_id": order_id,
            "customer_id": customer_id,
            "order_date": order_date.strftime("%Y-%m-%d"),
            "status": random.choice(statuses),
            "channel": random.choice(channels),
            "discount_pct": discount_pct,
            "shipping_city": customers_list[customer_id-1]["city"],
        })
        order_id += 1

orders = pd.DataFrame(orders_list)

# ─── 5. ORDER ITEMS ───────────────────────────────────────────────────────────
order_items_list = []
item_id = 1

for _, order in orders.iterrows():
    n_items = random.choices([1, 2, 3, 4], weights=[50, 30, 15, 5])[0]
    products_chosen = random.sample(range(1, 51), n_items)
    
    for product_id in products_chosen:
        product = products[products["product_id"] == product_id].iloc[0]
        quantity = random.choices([1, 2, 3], weights=[70, 20, 10])[0]
        unit_price = float(product["price"])
        discount_pct = order["discount_pct"]
        subtotal = round(unit_price * quantity * (1 - discount_pct / 100), 2)
        
        order_items_list.append({
            "item_id": item_id,
            "order_id": order["order_id"],
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": unit_price,
            "discount_pct": discount_pct,
            "subtotal": subtotal
        })
        item_id += 1

order_items = pd.DataFrame(order_items_list)

# Adauga total_amount la orders
order_totals = order_items.groupby("order_id")["subtotal"].sum().reset_index()
order_totals.columns = ["order_id", "total_amount"]
orders = orders.merge(order_totals, on="order_id", how="left")
orders["total_amount"] = orders["total_amount"].round(2)

# ─── SALVEAZA IN DB ───────────────────────────────────────────────────────────
categories.to_sql("categories", engine, index=False, if_exists="replace")
products.to_sql("products", engine, index=False, if_exists="replace")
customers.to_sql("customers", engine, index=False, if_exists="replace")
orders.to_sql("orders", engine, index=False, if_exists="replace")
order_items.to_sql("order_items", engine, index=False, if_exists="replace")

# ─── SUMMARY ──────────────────────────────────────────────────────────────────
print("=" * 55)
print("  E-COMMERCE DATABASE CREAT CU SUCCES")
print("=" * 55)
print(f"\n  Locatie: {db_path}")
print(f"\n  Tabele:")
print(f"    categories  →  {len(categories):>4} randuri")
print(f"    products    →  {len(products):>4} randuri")
print(f"    customers   →  {len(customers):>4} randuri")
print(f"    orders      →  {len(orders):>4} randuri")
print(f"    order_items →  {len(order_items):>4} randuri")
print(f"\n  Total:         {len(categories)+len(products)+len(customers)+len(orders)+len(order_items):>4} randuri")
print("\n  Cum conectezi in DBeaver:")
print("  1. New Database Connection")
print("  2. Alege SQLite")
print("  3. Path → selecteaza ecommerce.db")
print("  4. Test Connection → Finish")
print("\n  Schema:")
print("  customers → orders → order_items ← products → categories")
print("=" * 55)
