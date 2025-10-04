from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter(prefix='/productos', tags=['productos'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/', response_model=schemas.Producto)
def create_producto(prod: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.create_producto(db, prod)

@router.get('/', response_model=list[schemas.Producto])
def list_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_productos(db, skip, limit)

@router.get('/{producto_id}', response_model=schemas.Producto)
def get_producto(producto_id: int, db: Session = Depends(get_db)):
    p = crud.get_producto(db, producto_id)
    if not p:
        raise HTTPException(status_code=404, detail='Producto no encontrado')
    return p

@router.put('/{producto_id}', response_model=schemas.Producto)
def update_producto(producto_id: int, prod: schemas.ProductoCreate, db: Session = Depends(get_db)):
    p = crud.update_producto(db, producto_id, prod)
    if not p:
        raise HTTPException(status_code=404, detail='Producto no encontrado')
    return p

@router.delete('/{producto_id}')
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_producto(db, producto_id)
    if not ok:
        raise HTTPException(status_code=404, detail='Producto no encontrado')
    return { 'ok': True }
