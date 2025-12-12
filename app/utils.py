# app/utils.py
import re
from passlib.context import CryptContext
from bson import ObjectId
from datetime import datetime, timedelta
import os
import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
JWT_SECRET = os.getenv("JWT_SECRET", "super-secret-key")
JWT_ALGORITHM = "HS256"
JWT_EXP_MINUTES = 60

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain, hashed) -> bool:
    return pwd_context.verify(plain, hashed)

def create_jwt(payload: dict) -> str:
    exp = datetime.utcnow() + timedelta(minutes=int(os.getenv("JWT_EXP_MINUTES", JWT_EXP_MINUTES)))
    payload.update({"exp": exp})
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def sanitize_org_name(name: str) -> str:
    # keep lowercase alphanum and underscore
    name = name.strip().lower()
    name = re.sub(r'[^a-z0-9_]', '_', name)
    return name

def oid_to_str(oid):
    return str(oid) if isinstance(oid, ObjectId) else oid
