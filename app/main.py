# app/main.py
from fastapi import FastAPI
from .routes.org_routes import router as org_router
from .routes.admin_routes import router as admin_router

app = FastAPI(title="Organization Management Service")

# root / health endpoint
@app.get("/", tags=["root"])
async def root():
    return {"status": "ok", "message": "Organization Management Service is running"}

# register routers (they will be available under the prefixes defined in the router files)
app.include_router(org_router)
app.include_router(admin_router)
