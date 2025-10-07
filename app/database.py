from sqlalchemy import text

def init_db():
    sql_path = os.path.join(os.path.dirname(__file__), "..", "sql", "init_db.sql")
    if os.path.exists(sql_path):
        with engine.connect() as connection:
            with open(sql_path, "r", encoding="utf-8") as f:
                sql_commands = f.read()
            connection.execute(text(sql_commands))
            connection.commit()
            print("✅ Base de datos inicializada con init_db.sql")
    else:
        print("⚠️ No se encontró init_db.sql")

# Ejecutar init_db() al iniciar (solo la primera vez)
try:
    init_db()
except Exception as e:
    print(f"Error al inicializar la base de datos: {e}")
