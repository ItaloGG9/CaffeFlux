from pydantic import BaseModel
from typing import Optional, List
from decimal import Decimal
from datetime import datetime

class JerarquiaBase(BaseModel):
    nombre_jerarquia: str
    id_categoria: Optional[int] = None
    id_subcategoria: Optional[int] = None
    estado: Optional[bool] = True

class JerarquiaCreate(JerarquiaBase):
    pass

class Jerarquia(JerarquiaBase):
    id_jerarquia: int
    class Config:
        orm_mode = True

class ProductoBase(BaseModel):
    nombre_producto: str
    precio_venta: Decimal
    precio_costo: Decimal
    jerarquia: Optional[str] = None
    estado_producto: Optional[bool] = True
    id_jerarquia: Optional[int] = None

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    id_producto: int
    class Config:
        orm_mode = True

class MesaBase(BaseModel):
    estado_mesa: Optional[str] = None
    hora_apertura: Optional[datetime] = None
    hora_cierre: Optional[datetime] = None
    observaciones: Optional[str] = None

class MesaCreate(MesaBase):
    pass

class Mesa(MesaBase):
    id_mesa: int
    class Config:
        orm_mode = True

class LineaPedidoBase(BaseModel):
    id_producto: int

class LineaPedidoCreate(LineaPedidoBase):
    pass

class LineaPedido(LineaPedidoBase):
    id_linea: int
    id_pedido: int
    class Config:
        orm_mode = True

class PedidoBase(BaseModel):
    id_mesa: Optional[int] = None
    metodo_pago: Optional[str] = None
    propina: Optional[Decimal] = None
    descuento: Optional[Decimal] = None
    total: Optional[Decimal] = None

class PedidoCreate(PedidoBase):
    lineas: Optional[List[LineaPedidoCreate]] = []

class Pedido(PedidoBase):
    id_pedido: int
    hora_creacion: Optional[datetime] = None
    lineas: List[LineaPedido] = []
    class Config:
        orm_mode = True

class TurnoBase(BaseModel):
    usuario_responsable: str
    hora_apertura: Optional[datetime] = None
    fondo_inicial: Optional[Decimal] = None

class TurnoCreate(TurnoBase):
    pass

class Turno(TurnoBase):
    id_turno: int
    hora_cierre: Optional[datetime] = None
    usuario_cierre: Optional[str] = None
    class Config:
        orm_mode = True

class PagoBase(BaseModel):
    id_pedido: int
    metodo_pago: str
    monto: Decimal

class PagoCreate(PagoBase):
    pass

class Pago(PagoBase):
    id_pago: int
    fecha_hora: Optional[datetime] = None
    class Config:
        orm_mode = True
