from sqlalchemy import Column, Integer, String, Numeric, Boolean, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class JerarquiaProducto(Base):
    __tablename__ = 'jerarquia_productos'
    id_jerarquia = Column(Integer, primary_key=True, index=True)
    nombre_jerarquia = Column(String(100), nullable=False)
    id_categoria = Column(Integer)
    id_subcategoria = Column(Integer)
    estado = Column(Boolean, default=True)

    productos = relationship('Producto', back_populates='jerarquia_obj')

class Producto(Base):
    __tablename__ = 'productos'
    id_producto = Column(Integer, primary_key=True, index=True)
    nombre_producto = Column(String(100), nullable=False)
    precio_venta = Column(Numeric(10,2), nullable=False)
    precio_costo = Column(Numeric(10,2), nullable=False)
    jerarquia = Column(String(50))
    estado_producto = Column(Boolean, default=True)
    id_jerarquia = Column(Integer, ForeignKey('jerarquia_productos.id_jerarquia'))

    jerarquia_obj = relationship('JerarquiaProducto', back_populates='productos')

class Mesa(Base):
    __tablename__ = 'mesas'
    id_mesa = Column(Integer, primary_key=True, index=True)
    estado_mesa = Column(String(50))
    hora_apertura = Column(TIMESTAMP)
    hora_cierre = Column(TIMESTAMP)
    observaciones = Column(Text)

    pedidos = relationship('Pedido', back_populates='mesa_obj')

class Pedido(Base):
    __tablename__ = 'pedidos'
    id_pedido = Column(Integer, primary_key=True, index=True)
    id_mesa = Column(Integer, ForeignKey('mesas.id_mesa'))
    hora_creacion = Column(TIMESTAMP)
    metodo_pago = Column(String(50))
    propina = Column(Numeric(10,2))
    descuento = Column(Numeric(10,2))
    total = Column(Numeric(10,2))

    mesa_obj = relationship('Mesa', back_populates='pedidos')
    lineas = relationship('LineaPedido', back_populates='pedido', cascade='all, delete-orphan')
    pagos = relationship('Pago', back_populates='pedido')

class LineaPedido(Base):
    __tablename__ = 'lineas_pedido'
    id_linea = Column(Integer, primary_key=True, index=True)
    id_pedido = Column(Integer, ForeignKey('pedidos.id_pedido', ondelete='CASCADE'))
    id_producto = Column(Integer, ForeignKey('productos.id_producto'))

    pedido = relationship('Pedido', back_populates='lineas')
    producto = relationship('Producto')

class Turno(Base):
    __tablename__ = 'turnos'
    id_turno = Column(Integer, primary_key=True, index=True)
    usuario_responsable = Column(String(50))
    hora_apertura = Column(TIMESTAMP)
    fondo_inicial = Column(Numeric(10,2))
    hora_cierre = Column(TIMESTAMP)
    usuario_cierre = Column(String(50))

class Pago(Base):
    __tablename__ = 'pagos'
    id_pago = Column(Integer, primary_key=True, index=True)
    id_pedido = Column(Integer, ForeignKey('pedidos.id_pedido'))
    metodo_pago = Column(String(50))
    monto = Column(Numeric(10,2))
    fecha_hora = Column(TIMESTAMP)

    pedido = relationship('Pedido', back_populates='pagos')
