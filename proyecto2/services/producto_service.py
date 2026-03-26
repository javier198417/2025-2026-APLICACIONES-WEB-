from models.producto import Producto

class ProductoService:
    def __init__(self, db_connection):
        self.db = db_connection

    def listar(self):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos")
        rows = cursor.fetchall()
        cursor.close()
        return [Producto(**row) for row in rows]

    def obtener_por_id(self, id_producto):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos WHERE id_producto = %s", (id_producto,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Producto(**row)
        return None

    def crear(self, producto):
        cursor = self.db.connection.cursor()
        cursor.execute(
            """INSERT INTO productos 
               (nombre, descripcion, precio, stock, id_categoria, fecha_registro) 
               VALUES (%s, %s, %s, %s, %s, NOW())""",
            (producto.nombre, producto.descripcion, producto.precio,
             producto.stock, producto.id_categoria)
        )
        self.db.connection.commit()
        producto.id_producto = cursor.lastrowid
        cursor.close()
        return producto

    def actualizar(self, producto):
        cursor = self.db.connection.cursor()
        cursor.execute(
            """UPDATE productos 
               SET nombre=%s, descripcion=%s, precio=%s, stock=%s, id_categoria=%s 
               WHERE id_producto=%s""",
            (producto.nombre, producto.descripcion, producto.precio,
             producto.stock, producto.id_categoria, producto.id_producto)
        )
        self.db.connection.commit()
        cursor.close()

    def eliminar(self, id_producto):
        cursor = self.db.connection.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
        self.db.connection.commit()
        cursor.close()