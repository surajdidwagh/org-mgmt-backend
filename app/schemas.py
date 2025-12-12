# app/schemas.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class OrgCreate(BaseModel):
    organization_name: str = Field(..., min_length=3)
    email: EmailStr
    password: str

class OrgGet(BaseModel):
    organization_name: str

class OrgUpdate(BaseModel):
    organization_name: str
    email: Optional[EmailStr]
    password: Optional[str]

class AdminLogin(BaseModel):
    email: EmailStr
    password: str

class OrgOut(BaseModel):
    organization_name: str
    collection_name: str
    admin_id: str
