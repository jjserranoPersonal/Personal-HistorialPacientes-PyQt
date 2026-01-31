from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Archivo(Base):
    __tablename__ = "archivos"
    
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id", ondelete="CASCADE"), nullable=False)
    nombre_archivo = Column(String(255), nullable=False)
    tipo_archivo = Column(String(50))
    ruta_archivo = Column(String(500), nullable=False)
    tamano_bytes = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(Integer, ForeignKey("usuarios.id"))
    
    # Relationships
    paciente = relationship("Paciente", back_populates="archivos")
