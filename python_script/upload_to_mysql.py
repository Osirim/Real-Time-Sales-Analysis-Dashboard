from database import get_connection

conn = get_connection()
cursor = conn.cursor()

def upload_sale(data):
    query = """
    INSERT INTO sales (
        order_id,
        order_date,
        customer_name,
        segment,
        region,
        city,
        category,
        sub_category,
        product_name,
        quantity,
        sales,
        profit
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data["order_id"],
        data["order_date"],
        data["customer_name"],
        data["segment"],
        data["region"],
        data["city"],
        data["category"],
        data["sub_category"],
        data["product_name"],
        data["quantity"],
        data["sales"],
        data["profit"]
    )

    cursor.execute(query, values)
    conn.commit()