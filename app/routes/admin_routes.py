# app/routes/admin_routes.py
from fastapi import APIRouter, HTTPException
from ..schemas import AdminLogin
from ..auth import admin_login

router = APIRouter(prefix="/admin", tags=["admin"])

@router.post("/login")
async def login(payload: AdminLogin):
    token = await admin_login(payload.email, payload.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token}
