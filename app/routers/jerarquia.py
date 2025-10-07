from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter(prefix='/jerarquia', tags=['jerarquia'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/', response_model=schemas.Jerarquia)
def create_jerarquia(j: schemas.JerarquiaCreate, db: Session = Depends(get_db)):
    return crud.create_jerarquia(db, j)

@router.get('/', response_model=list[schemas.Jerarquia])
def list_jerarquias(db: Session = Depends(get_db)):
    return crud.get_jerarquias(db)
