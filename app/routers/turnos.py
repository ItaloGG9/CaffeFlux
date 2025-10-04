from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud
from .. import models

router = APIRouter(prefix='/turnos', tags=['turnos'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/', response_model=schemas.Turno)
def abrir_turno(t: schemas.TurnoCreate, db: Session = Depends(get_db)):
    db_t = models.Turno(usuario_responsable=t.usuario_responsable, hora_apertura=t.hora_apertura, fondo_inicial=t.fondo_inicial)
    db.add(db_t); db.commit(); db.refresh(db_t)
    return db_t
