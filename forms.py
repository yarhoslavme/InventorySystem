from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class formulario_login(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message="Nombre de usuario requerido")])
    password = PasswordField('Contraseña', validators=[DataRequired(message="Contraseña requerida")])
    enviar = SubmitField('Iniciar Sesión')

