from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.core.database import get_db
from app.models.paciente import Paciente
from app.models.usuario import Usuario
from app.schemas.paciente import Paciente as PacienteSchema, PacienteCreate, PacienteUpdate
from app.api.deps import get_current_user

router = APIRouter()


@router.get("/", response_model=List[PacienteSchema])
def list_pacientes(
    skip: int = 0,
    limit: int = 20,
    nombre: str = None,
    identificacion: str = None,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
) -> Any:
    """
    Listar pacientes con paginación y filtros opcionales.
    """
    query = db.query(Paciente)
    
    if nombre:
        query = query.filter(
            or_(
                Paciente.nombres.ilike(f"%{nombre}%"),
                Paciente.apellidos.ilike(f"%{nombre}%")
            )
        )
    
    if identificacion:
        query = query.filter(Paciente.identificacion == identificacion)
    
    pacientes = query.offset(skip).limit(min(limit, 100)).all()
    return pacientes


@router.get("/{paciente_id}", response_model=PacienteSchema)
def get_paciente(
    paciente_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
) -> Any:
    """
    Obtener paciente por ID.
    """
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente no encontrado"
        )
    return paciente


@router.post("/", response_model=PacienteSchema, status_code=status.HTTP_201_CREATED)
def create_paciente(
    paciente_in: PacienteCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
) -> Any:
    """
    Crear nuevo paciente.
    """
    # Verificar que no exista paciente con misma identificación
    existing = db.query(Paciente).filter(
        Paciente.identificacion == paciente_in.identificacion
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Paciente con esta identificación ya existe"
        )
    
    paciente = Paciente(
        **paciente_in.model_dump(),
        created_by=current_user.id
    )
    db.add(paciente)
    db.commit()
    db.refresh(paciente)
    return paciente


@router.put("/{paciente_id}", response_model=PacienteSchema)
def update_paciente(
    paciente_id: int,
    paciente_in: PacienteUpdate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
) -> Any:
    """
    Actualizar paciente existente.
    """
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente no encontrado"
        )
    
    # Si se actualiza identificación, verificar que no exista
    if paciente_in.identificacion and paciente_in.identificacion != paciente.identificacion:
        existing = db.query(Paciente).filter(
            Paciente.identificacion == paciente_in.identificacion
        ).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Paciente con esta identificación ya existe"
            )
    
    update_data = paciente_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(paciente, field, value)
    
    db.add(paciente)
    db.commit()
    db.refresh(paciente)
    return paciente


@router.delete("/{paciente_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_paciente(
    paciente_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
) -> None:
    """
    Eliminar paciente (soft delete o hard delete según configuración).
    """
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente no encontrado"
        )
    
    db.delete(paciente)
    db.commit()
    return None
