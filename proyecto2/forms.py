from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, FloatField, IntegerField, SelectField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional, EqualTo

class ContactoForm(FlaskForm):
    """ Formulario para contacto/guardar en archivos """
    nombre = StringField(
        'Nombre',
        validators=[
            DataRequired(message='El nombre es obligatorio'),
            Length(min=2, max=100, message='El nombre debe tener entre 2 y 100 caracteres')
        ],
        render_kw={"placeholder": "Ingresa tu nombre completo"}
    )
    
    email = EmailField(
        'Email',
        validators=[
            DataRequired(message='El email es obligatorio'),
            Email(message='Ingresa un email válido')
        ],
        render_kw={"placeholder": "correo@ejemplo.com"}
    )
    
    mensaje = TextAreaField(
        'Mensaje',
        validators=[
            DataRequired(message='El mensaje es obligatorio'),
            Length(min=5, max=500, message='El mensaje debe tener entre 5 y 500 caracteres')
        ],
        render_kw={"placeholder": "Escribe tu mensaje aquí...", "rows": 5}
    )
    
    submit_txt = SubmitField('Guardar en TXT')
    submit_json = SubmitField('Guardar en JSON')
    submit_csv = SubmitField('Guardar en CSV')

class ProductoForm(FlaskForm):
    """ Formulario para gestión de productos en MySQL """
    nombre = StringField(
        'Nombre del Producto', 
        validators=[DataRequired(message='El nombre es obligatorio')],
        render_kw={"placeholder": "Ej. Laptop Gamer"}
    )
    
    precio = FloatField(
        'Precio', 
        validators=[
            DataRequired(message='El precio es obligatorio'),
            NumberRange(min=0.01, message='El precio debe ser mayor a 0')
        ],
        render_kw={"placeholder": "0.00", "step": "0.01"}
    )
    
    stock = IntegerField(
        'Stock / Cantidad',
        validators=[
            DataRequired(message='La cantidad es obligatoria'),
            NumberRange(min=0, message='La cantidad no puede ser negativa')
        ],
        render_kw={"placeholder": "0", "min": "0"}
    )
    
    id_categoria = SelectField(
        'Categoría', 
        coerce=int, 
        validators=[DataRequired(message='Selecciona una categoría')]
    )
    
    submit = SubmitField('Guardar Producto')

class RegistroForm(FlaskForm):
    """ Formulario para registro de nuevos usuarios """
    nombre = StringField(
        'Nombre',
        validators=[
            DataRequired(message='El nombre es obligatorio'),
            Length(min=2, max=100, message='El nombre debe tener entre 2 y 100 caracteres')
        ],
        render_kw={"placeholder": "Tu nombre completo"}
    )
    
    email = EmailField(
        'Email',
        validators=[
            DataRequired(message='El email es obligatorio'),
            Email(message='Ingresa un email válido')
        ],
        render_kw={"placeholder": "correo@ejemplo.com"}
    )
    
    password = PasswordField(
        'Contraseña',
        validators=[
            DataRequired(message='La contraseña es obligatoria'),
            Length(min=6, message='La contraseña debe tener al menos 6 caracteres')
        ],
        render_kw={"placeholder": "********"}
    )
    
    confirm_password = PasswordField(
        'Confirmar Contraseña',
        validators=[
            DataRequired(message='Debes confirmar la contraseña'),
            EqualTo('password', message='Las contraseñas deben coincidir')
        ],
        render_kw={"placeholder": "********"}
    )
    
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    """ Formulario para inicio de sesión """
    email = EmailField(
        'Email',
        validators=[
            DataRequired(message='El email es obligatorio'),
            Email(message='Ingresa un email válido')
        ],
        render_kw={"placeholder": "correo@ejemplo.com"}
    )
    
    password = PasswordField(
        'Contraseña',
        validators=[DataRequired(message='La contraseña es obligatoria')],
        render_kw={"placeholder": "********"}
    )
    
    submit = SubmitField('Iniciar Sesión')
