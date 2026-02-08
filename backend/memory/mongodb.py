# from pymongo import MongoClient
from pymongo import MongoClient
from backend.config import MONGODB_URI

client = MongoClient(MONGODB_URI)
db = client["voxaAI"]

users_col = db["users"]
sessions_col = db["sessions"]            
orders_col = db["orders"]
payments_col = db["payments"]
