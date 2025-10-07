-- Script para crear las tablas en PostgreSQL

-- Ejecuta este script conectado a la base de datos `caffe_flux`.

CREATE TABLE IF NOT EXISTS jerarquia_productos (
    id_jerarquia SERIAL PRIMARY KEY,
    nombre_jerarquia VARCHAR(100) NOT NULL,
    id_categoria INT,
    id_subcategoria INT,
    estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS productos (
    id_producto SERIAL PRIMARY KEY,
    nombre_producto VARCHAR(100) NOT NULL,
    precio_venta DECIMAL(10,2) NOT NULL,
    precio_costo DECIMAL(10,2) NOT NULL,
    jerarquia VARCHAR(50),
    estado_producto BOOLEAN DEFAULT TRUE,
    id_jerarquia INT REFERENCES jerarquia_productos(id_jerarquia)
);

CREATE TABLE IF NOT EXISTS mesas (
    id_mesa SERIAL PRIMARY KEY,
    estado_mesa VARCHAR(50),
    hora_apertura TIMESTAMP,
    hora_cierre TIMESTAMP,
    observaciones TEXT
);

CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido SERIAL PRIMARY KEY,
    id_mesa INT REFERENCES mesas(id_mesa),
    hora_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metodo_pago VARCHAR(50),
    propina DECIMAL(10,2),
    descuento DECIMAL(10,2),
    total DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS lineas_pedido (
    id_linea SERIAL PRIMARY KEY,
    id_pedido INT REFERENCES pedidos(id_pedido) ON DELETE CASCADE,
    id_producto INT REFERENCES productos(id_producto)
);

CREATE TABLE IF NOT EXISTS turnos (
    id_turno SERIAL PRIMARY KEY,
    usuario_responsable VARCHAR(50),
    hora_apertura TIMESTAMP,
    fondo_inicial DECIMAL(10,2),
    hora_cierre TIMESTAMP,
    usuario_cierre VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS pagos (
    id_pago SERIAL PRIMARY KEY,
    id_pedido INT REFERENCES pedidos(id_pedido),
    metodo_pago VARCHAR(50),
    monto DECIMAL(10,2),
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
