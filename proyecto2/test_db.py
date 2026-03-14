from app import app, db
from sqlalchemy import inspect

with app.app_context():
    print("🔌 URI de conexión:", db.engine.url)
    
    # Intentar crear las tablas
    db.create_all()
    print("✅ Tablas creadas (si no existían)")
    
    # Listar tablas existentes
    inspector = inspect(db.engine)
    tablas = inspector.get_table_names()
    print("📋 Tablas en la base de datos:", tablas)
    
    if 'productos' in tablas:
        print("🎉 ¡La tabla 'productos' existe!")
    else:
        print("❌ La tabla 'productos' NO existe.")