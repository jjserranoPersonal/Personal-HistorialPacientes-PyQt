from fastapi import APIRouter
from app.api.v1.endpoints import auth, pacientes, eventos

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(pacientes.router, prefix="/pacientes", tags=["pacientes"])
api_router.include_router(eventos.router, prefix="/eventos", tags=["eventos"])
