from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.evento import Evento
from app.models.paciente import Paciente
from app.models.usuario import Usuario
from app.schemas.evento import Evento as EventoSchema, EventoCreate
from app.api.deps import get_current_user

router = APIRouter()


@router.get("/", response_model=List[EventoSchema])
def list_eventos(
    skip: int = 0,
    limit: int = 20,
    paciente_id: int = None,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
) -> Any:
    """
    Listar eventos con paginación y filtro opcional por paciente.
    """
    query = db.query(Evento)
    
    if paciente_id:
        query = query.filter(Evento.paciente_id == paciente_id)
    
    eventos = query.order_by(Evento.created_at.desc()).offset(skip).limit(min(limit, 100)).all()
    return eventos


@router.get("/{evento_id}", response_model=EventoSchema)
def get_evento(
    evento_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
) -> Any:
    """
    Obtener evento por ID.
    """
    evento = db.query(Evento).filter(Evento.id == evento_id).first()
    if not evento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Evento no encontrado"
        )
    return evento


@router.post("/", response_model=EventoSchema, status_code=status.HTTP_201_CREATED)
def create_evento(
    evento_in: EventoCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
) -> Any:
    """
    Crear nuevo evento médico.
    """
    # Verificar que el paciente existe
    paciente = db.query(Paciente).filter(Paciente.id == evento_in.paciente_id).first()
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente no encontrado"
        )
    
    evento = Evento(
        **evento_in.model_dump(),
        created_by=current_user.id
    )
    db.add(evento)
    db.commit()
    db.refresh(evento)
    return evento


@router.get("/pacientes/{paciente_id}/historial", response_model=List[EventoSchema])
def get_historial_paciente(
    paciente_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
) -> Any:
    """
    Obtener historial completo de eventos de un paciente.
    Ordenado por fecha descendente (más reciente primero).
    """
    # Verificar que el paciente existe
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente no encontrado"
        )
    
    eventos = db.query(Evento).filter(
        Evento.paciente_id == paciente_id
    ).order_by(Evento.created_at.desc()).all()
    
    return eventos
