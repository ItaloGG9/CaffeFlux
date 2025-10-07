from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter(prefix='/pedidos', tags=['pedidos'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/', response_model=schemas.Pedido)
def create_pedido(p: schemas.PedidoCreate, db: Session = Depends(get_db)):
    return crud.create_pedido(db, p)

@router.get('/', response_model=list[schemas.Pedido])
def list_pedidos(db: Session = Depends(get_db)):
    return crud.get_pedidos(db)
