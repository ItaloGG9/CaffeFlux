from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter(prefix='/pagos', tags=['pagos'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/', response_model=schemas.Pago)
def create_pago(p: schemas.PagoCreate, db: Session = Depends(get_db)):
    return crud.create_pago(db, p)
