# app/crud.py
from .database import master_org_col, admin_col, db
from .utils import hash_password, sanitize_org_name, oid_to_str
from datetime import datetime
from bson import ObjectId

async def org_exists(org_name: str) -> bool:
    return await master_org_col.find_one({"organization_name": org_name}) is not None

async def create_organization(org_name: str, email: str, password: str):
    if await org_exists(org_name):
        raise ValueError("Organization already exists")
    coll_name = f"org_{sanitize_org_name(org_name)}"
    # create admin user
    admin_doc = {
        "email": email,
        "password_hash": hash_password(password),
        "created_at": datetime.utcnow(),
    }
    admin_res = await admin_col.insert_one(admin_doc)
    admin_id = admin_res.inserted_id
    org_doc = {
        "organization_name": org_name,
        "collection_name": coll_name,
        "admin_id": admin_id,
        "created_at": datetime.utcnow()
    }
    res = await master_org_col.insert_one(org_doc)
    # programmatically create the collection (Mongo creates on first insert; optionally create an index)
    await db[coll_name].insert_one({"_meta": "initialized", "created_at": datetime.utcnow()})
    # optionally remove the initializer doc
    await db[coll_name].delete_one({"_meta": "initialized"})
    return {**org_doc, "_id": res.inserted_id}

async def get_org(org_name: str):
    doc = await master_org_col.find_one({"organization_name": org_name})
    if not doc:
        return None
    doc["admin_id"] = oid_to_str(doc["admin_id"])
    doc["_id"] = oid_to_str(doc["_id"])
    return doc

async def delete_org(org_name: str):
    doc = await master_org_col.find_one({"organization_name": org_name})
    if not doc:
        raise ValueError("Org not found")
    coll = doc["collection_name"]
    # drop collection
    await db[coll].drop()
    # delete admin
    await admin_col.delete_one({"_id": doc["admin_id"]})
    # delete metadata
    await master_org_col.delete_one({"_id": doc["_id"]})
    return True
