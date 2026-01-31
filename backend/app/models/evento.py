from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Evento(Base):
    __tablename__ = "eventos"
    
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id", ondelete="CASCADE"), nullable=False)
    estado = Column(Text)
    hea = Column(Text)  # Historia enfermedad actual
    imp_diagnostica = Column(Text)  # Impresión diagnóstica
    conducta_seguir = Column(Text)
    motivo_consulta = Column(Text)
    temperatura = Column(String(20))
    tension_arterial = Column(String(20))
    fre_cardiaca = Column(String(20))
    fre_respiratoria = Column(String(20))
    oxigenacion = Column(String(20))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(Integer, ForeignKey("usuarios.id"))
    
    # Relationships
    paciente = relationship("Paciente", back_populates="eventos")
