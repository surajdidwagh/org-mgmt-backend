# app/database.py
from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MASTER_DB", "org_master_db")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

# master collections
master_org_col = db["organizations_master"]
admin_col = db["admins"]
