import random
from datetime import datetime

customers = [
    "John Doe",
    "Mary Johnson",
    "David Smith",
    "Sarah Williams",
    "Michael Brown",
    "Daniel Wilson"
]

segments = [
    "Consumer",
    "Corporate",
    "Home Office"
]

regions = [
    "West",
    "East",
    "North",
    "South"
]

cities = [
    "Lagos",
    "Abuja",
    "Portharcourt",
    "Ibadan"
]

products = [
    {
        "category":"Technology",
        "sub_category":"Phones",
        "product_name":"iPhone 14",
        "sales_range":(700000,1200000),
        "profit_range":(50000,200000)
    },
    {
        "category":"Technology",
        "sub_category":"Laptops",
        "product_name":"HP EliteBook",
        "sales_range":(450000,900000),
        "profit_range":(40000,150000)
    },
    {
        "category":"Furniture",
        "sub_category":"Chairs",
        "product_name":"Office Chair",
        "sales_range":(50000,150000),
        "profit_range":(5000,25000)
    },
    {
        "category":"Office Supplies",
        "sub_category":"Binders",
        "product_name":"Premium Binder",
        "sales_range":(5000,20000),
        "profit_range":(1000,5000)
    },
    {
        "category":"Office Supplies",
        "sub_category":"Paper",
        "product_name":"A4 Printing Paper",
        "sales_range":(3000,10000),
        "profit_range":(500,3000)
    }
]

def generate_sale():

    product = random.choice(products)

    return {
        "order_id": f"ORD-{random.randint(10000,999999)}",
        "order_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "customer_name": random.choice(customers),
        "segment": random.choice(segments),
        "region": random.choice(regions),
        "city": random.choice(cities),
        "category": product["category"],
        "sub_category": product["sub_category"],
        "product_name": product["product_name"],
        "quantity": random.randint(1,5),
        "sales": random.randint(*product["sales_range"]),
        "profit": random.randint(*product["profit_range"])
    }