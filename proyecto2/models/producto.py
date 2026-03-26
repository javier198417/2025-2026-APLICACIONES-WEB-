class Producto:
    def __init__(self, id_producto=None, nombre=None, descripcion=None, precio=None,
                 stock=None, id_categoria=None, fecha_registro=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.id_categoria = id_categoria
        self.fecha_registro = fecha_registro  # puede ser None si no se asigna

    def to_dict(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'stock': self.stock,
            'id_categoria': self.id_categoria,
            'fecha_registro': self.fecha_registro
        }