# CaffeFlux Backend (Ready for Railway)

Proyecto backend en **FastAPI + SQLAlchemy** preparado para desplegar en Railway (o funcionar localmente).

## Estructura
```
CaffeFlux-backend/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routers/
│       ├── products.py
│       ├── jerarquia.py
│       ├── mesas.py
│       ├── pedidos.py
│       ├── turnos.py
│       └── pagos.py
├── requirements.txt
├── Procfile
├── .env.example
├── sql/
│   └── init_db.sql
└── README.md
```

## Instrucciones locales

1. Crear entorno virtual y activarlo:
- PowerShell (VSCode):
```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Instalar dependencias:
```
pip install -r requirements.txt
```

3. Configurar `.env` (puedes copiar `.env.example`):
```
DATABASE_URL=postgresql+psycopg2://usuario:password@localhost:5432/caffe_flux
```
Si usas PostgreSQL local, crea la base `caffe_flux` o cambia la URL.

4. Ejecutar:
```
uvicorn app.main:app --reload
```

La documentación interactiva estará en `http://127.0.0.1:8000/docs`

## Despliegue en Railway
1. Subir este repositorio a GitHub.
2. Crear un proyecto en Railway y añadir un plugin PostgreSQL.
3. En Settings > Variables de entorno, añade `DATABASE_URL` que Railway te entrega (ej: `postgresql://...`).
4. Asegúrate del `Procfile` presente (ya incluido).
5. Railway detectará la app y ejecutará el comando del Procfile.

---
Si quieres, puedo crear el repositorio en GitHub por ti o preparar un pequeño set de datos iniciales para la BD.
