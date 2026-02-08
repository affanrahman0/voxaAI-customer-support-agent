# from memory.mongodb import users_col, orders_col, payments_col
from backend.memory.mongodb import users_col, orders_col, payments_col

users_col.insert_one({
    "user_id": "U1001",
    "name": "Affan Rahman",
    "email": "affan@email.com"
})

orders_col.insert_one({
    "order_id": "FK12346",
    "user_id": "U1001",
    "product": "Microwave",
    "delivery_status": "delivered",
    "expected_delivery_date": "2026-01-18",
    "delivery_date": "2026-01-17",
    "return_status": None,
    "refund_status": None
})

payments_col.insert_one({
    "order_id": "FK12346",
    "amount": 2999
})

print("MongoDB sample data inserted")
