from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas
from datetime import datetime

# Productos
def create_producto(db: Session, prod: schemas.ProductoCreate):
    db_prod = models.Producto(**prod.dict())
    db.add(db_prod)
    db.commit()
    db.refresh(db_prod)
    return db_prod

def get_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Producto).offset(skip).limit(limit).all()

def get_producto(db: Session, producto_id: int):
    return db.query(models.Producto).filter(models.Producto.id_producto == producto_id).first()

def update_producto(db: Session, producto_id: int, prod: schemas.ProductoCreate):
    db_prod = get_producto(db, producto_id)
    if not db_prod:
        return None
    for k, v in prod.dict().items():
        setattr(db_prod, k, v)
    db.commit()
    db.refresh(db_prod)
    return db_prod

def delete_producto(db: Session, producto_id: int):
    db_prod = get_producto(db, producto_id)
    if not db_prod:
        return False
    db.delete(db_prod)
    db.commit()
    return True

# Jerarquia
def create_jerarquia(db: Session, j: schemas.JerarquiaCreate):
    db_j = models.JerarquiaProducto(**j.dict())
    db.add(db_j)
    db.commit()
    db.refresh(db_j)
    return db_j

def get_jerarquias(db: Session):
    return db.query(models.JerarquiaProducto).all()

# Mesas y pedidos (simplificado)
def create_mesa(db: Session, m: schemas.MesaCreate):
    db_m = models.Mesa(**m.dict())
    db.add(db_m)
    db.commit()
    db.refresh(db_m)
    return db_m

def create_pedido(db: Session, p: schemas.PedidoCreate):
    db_p = models.Pedido(id_mesa=p.id_mesa, hora_creacion=datetime.utcnow(), metodo_pago=p.metodo_pago, propina=p.propina, descuento=p.descuento, total=p.total)
    db.add(db_p)
    db.commit()
    # crear lineas
    for linea in p.lineas or []:
        lp = models.LineaPedido(id_pedido=db_p.id_pedido, id_producto=linea.id_producto)
        db.add(lp)
    db.commit()
    db.refresh(db_p)
    return db_p

def get_pedidos(db: Session):
    return db.query(models.Pedido).all()

def create_pago(db: Session, pago: schemas.PagoCreate):
    db_p = models.Pago(**pago.dict())
    db.add(db_p)
    db.commit()
    db.refresh(db_p)
    return db_p
