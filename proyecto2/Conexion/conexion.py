# Archivo: Conexion/conexion.py

class Config:
    # 2.3. Configuración de parámetros de conexión
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''  # Vacío por defecto en XAMPP
    MYSQL_DB = 'inventario'
    
    # Cadena de conexión para SQLAlchemy usando el conector PyMySQL
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
