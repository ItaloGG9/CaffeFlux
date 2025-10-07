import os
from fastapi import FastAPI
from app.database import init_db  # porque database.py está dentro de /app
from dotenv import load_dotenv
from app.database import engine, Base
from app.routers import products, jerarquia, mesas, pedidos, turnos, pagos

load_dotenv()

app = FastAPI(title="CaffeFlux API")

# Crear tablas en el arranque (solo si la BD lo permite)
Base.metadata.create_all(bind=engine)

# Incluir routers
app.include_router(products.router)
app.include_router(jerarquia.router)
app.include_router(mesas.router)
app.include_router(pedidos.router)
app.include_router(turnos.router)
app.include_router(pagos.router)

@app.get("/")
def root():
    return {"service": "CaffeFlux backend", "status": "running"}
