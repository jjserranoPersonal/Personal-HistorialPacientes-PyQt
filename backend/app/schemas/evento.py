from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class EventoBase(BaseModel):
    paciente_id: int
    estado: Optional[str] = None
    hea: Optional[str] = None
    imp_diagnostica: Optional[str] = None
    conducta_seguir: Optional[str] = None
    motivo_consulta: Optional[str] = None
    temperatura: Optional[str] = None
    tension_arterial: Optional[str] = None
    fre_cardiaca: Optional[str] = None
    fre_respiratoria: Optional[str] = None
    oxigenacion: Optional[str] = None


class EventoCreate(EventoBase):
    pass


class Evento(EventoBase):
    id: int
    created_at: datetime
    created_by: Optional[int] = None
    
    class Config:
        from_attributes = True
