# app/auth.py
from .database import admin_col, master_org_col
from .utils import verify_password, create_jwt, oid_to_str
from bson import ObjectId

async def admin_login(email: str, password: str):
    admin = await admin_col.find_one({"email": email})
    if not admin:
        return None
    if not verify_password(password, admin["password_hash"]):
        return None
    # find the org this admin belongs to (simplified: look up master by admin_id)
    org = await master_org_col.find_one({"admin_id": admin["_id"]})
    payload = {
        "admin_id": oid_to_str(admin["_id"]),
        "org_id": oid_to_str(org["_id"]) if org else None,
        "org_name": org["organization_name"] if org else None
    }
    token = create_jwt(payload)
    return token
