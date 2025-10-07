from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter(prefix='/mesas', tags=['mesas'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/', response_model=schemas.Mesa)
def create_mesa(m: schemas.MesaCreate, db: Session = Depends(get_db)):
    return crud.create_mesa(db, m)
