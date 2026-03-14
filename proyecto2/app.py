from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import json
import csv

# Importación de configuración y formularios
from Conexion.conexion import Config 
from forms import ContactoForm, ProductoForm 

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'proyecto_final_ecuador_2026'

# Inicializar SQLAlchemy para la gestión de MySQL
db = SQLAlchemy(app)

# ==========================================
# 3. MODELOS / TABLAS (MySQL)
# ==========================================

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    mail = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id_categoria = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(50), nullable=False, unique=True)
    productos = db.relationship('Producto', backref='categoria_rel', lazy=True)

class Producto(db.Model):
    __tablename__ = 'productos'
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id_categoria'))
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

# ==========================================
# 4. RUTAS Y OPERACIONES CRUD
# ==========================================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contactos', methods=['GET', 'POST'])
def contactos():
    form = ContactoForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        email = form.email.data
        mensaje = form.mensaje.data
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ruta_csv = os.path.join('inventario', 'data', 'datos.csv')
        try:
            os.makedirs(os.path.dirname(ruta_csv), exist_ok=True)
            with open(ruta_csv, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([nombre, email, mensaje, fecha])
            flash('¡Mensaje enviado con éxito y guardado en CSV!', 'success')
            return redirect(url_for('leer_csv'))
        except Exception as e:
            flash(f'Error al guardar: {e}', 'danger')

    return render_template('contactos.html', form=form)

@app.route('/productos')
def lista_productos():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

@app.route('/producto/nuevo', methods=['GET', 'POST'])
def crear_producto():
    form = ProductoForm()
    
    # 1. Consultar categorías de la base de datos
    categorias = Categoria.query.all()
    
    # 2. Pasarlas al formulario (Tupla: valor_real, texto_que_se_ve)
    form.id_categoria.choices = [(c.id_categoria, c.nombre_categoria) for c in categorias]
    
    if form.validate_on_submit():
        nuevo_p = Producto(
            nombre=form.nombre.data,
            precio=form.precio.data,
            stock=form.stock.data,
            id_categoria=form.id_categoria.data
        )
        db.session.add(nuevo_p)
        db.session.commit()
        flash('Producto creado con éxito', 'success')
        return redirect(url_for('lista_productos'))
    
    return render_template('producto_form.html', form=form)

@app.route('/producto/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = Producto.query.get_or_404(id)
    form = ProductoForm(obj=producto) # Carga datos existentes
    
    # Recargar categorías para el select
    form.id_categoria.choices = [(c.id_categoria, c.nombre_categoria) for c in Categoria.query.all()]
    
    if form.validate_on_submit():
        producto.nombre = form.nombre.data
        producto.precio = form.precio.data
        producto.stock = form.stock.data
        producto.id_categoria = form.id_categoria.data
        db.session.commit()
        flash('Producto actualizado correctamente', 'info')
        return redirect(url_for('lista_productos'))
        
    return render_template('producto_form.html', form=form, producto=producto, titulo="Editar Producto")

@app.route('/producto/eliminar/<int:id>')
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    flash('Producto eliminado correctamente', 'warning')
    return redirect(url_for('lista_productos'))

# --- RUTAS DE LECTURA DE ARCHIVOS ---

@app.route('/leer-txt')
def leer_txt():
    datos = []
    ruta = os.path.join('inventario', 'data', 'datos.txt')
    if os.path.exists(ruta):
        with open(ruta, 'r', encoding='utf-8') as f:
            datos = [linea.strip() for linea in f.readlines()]
    return render_template('datos.html', datos=datos, formato='TXT')

@app.route('/leer-json')
def leer_json():
    datos = []
    ruta = os.path.join('inventario', 'data', 'datos.json')
    if os.path.exists(ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                datos = json.load(f)
        except: datos = []
    return render_template('datos.html', datos=datos, formato='JSON')

@app.route('/leer-csv')
def leer_csv():
    datos = []
    ruta = os.path.join('inventario', 'data', 'datos.csv')
    if os.path.exists(ruta):
        with open(ruta, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            datos = list(reader)
    return render_template('datos.html', datos=datos, formato='CSV')

@app.route('/leer-sqlite') # <-- Verifica que no tenga espacios ni letras diferentes
def leer_sqlite():
    datos = Producto.query.all()
    return render_template('datos.html', datos=datos, formato='MySQL')

# ==========================================
# INICIALIZACIÓN
# ==========================================

with app.app_context():
    try:
        db.create_all() 
        # Crear una categoría por defecto si no hay ninguna, para que el form no falle
        if not Categoria.query.first():
            cat_inicial = Categoria(nombre_categoria="General")
            db.session.add(cat_inicial)
            db.session.commit()
        print("✅ Sistema sincronizado correctamente con MySQL.")
    except Exception as e:
        print(f"❌ Error al conectar con la base de datos: {e}")

if __name__ == '__main__':
    app.run(debug=True)