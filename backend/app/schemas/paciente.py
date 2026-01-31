from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime


class PacienteBase(BaseModel):
    identificacion: str
    nombres: str
    apellidos: str
    direccion: Optional[str] = None
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    sexo: Optional[str] = None
    transfusiones: Optional[str] = None
    peso: Optional[str] = None
    talla: Optional[str] = None
    habitos_toxicos: Optional[str] = None
    alergia_medicamentos: Optional[str] = None
    vacunacion: Optional[str] = None
    app: Optional[str] = None
    apf: Optional[str] = None
    nombre_acompanante: Optional[str] = None


class PacienteCreate(PacienteBase):
    pass


class PacienteUpdate(BaseModel):
    identificacion: Optional[str] = None
    nombres: Optional[str] = None
    apellidos: Optional[str] = None
    direccion: Optional[str] = None
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    sexo: Optional[str] = None
    transfusiones: Optional[str] = None
    peso: Optional[str] = None
    talla: Optional[str] = None
    habitos_toxicos: Optional[str] = None
    alergia_medicamentos: Optional[str] = None
    vacunacion: Optional[str] = None
    app: Optional[str] = None
    apf: Optional[str] = None
    nombre_acompanante: Optional[str] = None


class Paciente(PacienteBase):
    id: int
    foto_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    created_by: Optional[int] = None
    
    class Config:
        from_attributes = True
