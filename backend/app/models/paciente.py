from sqlalchemy import Column, Integer, String, Date, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Paciente(Base):
    __tablename__ = "pacientes"
    
    id = Column(Integer, primary_key=True, index=True)
    identificacion = Column(String(50), unique=True, nullable=False, index=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    direccion = Column(String(200))
    correo = Column(String(100))
    telefono = Column(String(50))
    fecha_nacimiento = Column(Date)
    sexo = Column(String(1))
    transfusiones = Column(String(2))
    peso = Column(String(20))
    talla = Column(String(20))
    habitos_toxicos = Column(Text)
    alergia_medicamentos = Column(Text)
    vacunacion = Column(Text)
    app = Column(Text)  # Antecedentes personales patológicos
    apf = Column(Text)  # Antecedentes personales fisiológicos
    nombre_acompanante = Column(String(200))
    foto_url = Column(String(500))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    created_by = Column(Integer, ForeignKey("usuarios.id"))
    
    # Relationships
    eventos = relationship("Evento", back_populates="paciente", cascade="all, delete-orphan")
    archivos = relationship("Archivo", back_populates="paciente", cascade="all, delete-orphan")
