from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from app.core.database import Base


class AuditLog(Base):
    __tablename__ = "audit_log"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    accion = Column(String(50), nullable=False)
    tabla = Column(String(50), nullable=False)
    registro_id = Column(Integer)
    datos_anteriores = Column(JSONB)
    datos_nuevos = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
