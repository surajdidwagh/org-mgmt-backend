# app/routes/org_routes.py
from fastapi import APIRouter, HTTPException, Depends, Header
from ..schemas import OrgCreate, OrgGet, OrgUpdate, OrgOut
from ..crud import create_organization, get_org, delete_org, org_exists

router = APIRouter(prefix="/org", tags=["org"])

@router.post("/create", response_model=OrgOut)
async def create_org(payload: OrgCreate):
    if await org_exists(payload.organization_name):
        raise HTTPException(status_code=400, detail="Organization already exists")
    org = await create_organization(payload.organization_name, payload.email, payload.password)
    return {
        "organization_name": org["organization_name"],
        "collection_name": org["collection_name"],
        "admin_id": str(org["admin_id"])
    }

@router.get("/get", response_model=OrgOut)
async def get_organization(organization_name: str):
    doc = await get_org(organization_name)
    if not doc:
        raise HTTPException(status_code=404, detail="Organization not found")
    return {
        "organization_name": doc["organization_name"],
        "collection_name": doc["collection_name"],
        "admin_id": doc["admin_id"]
    }

@router.delete("/delete")
async def delete_organization(organization_name: str, authorization: str = Header(None)):
    # In production: parse JWT and verify admin belongs to org
    # simplified: require token and proceed (implement proper auth)
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing token")
    try:
        await delete_org(organization_name)
    except ValueError:
        raise HTTPException(status_code=404, detail="Org not found")
    return {"status": "deleted"}
