from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, csrf, EmailField, IntegerField

class LoginForm (FlaskForm):
  # Definir os campos do formulário com os respectivos validadores
  email = EmailField ('Email', validators=[validators.DataRequired (), validators.Length (min=3, max=50, message='O email deve ter no mínimo 3 caracteres e no máximo 50!')])
  password = PasswordField ('Senha', validators=[validators.DataRequired (), validators.Length (min=6, max=25, message='A senha deve ter entre 6 e 25 caracteres!')])

class RegisterForm (FlaskForm):
  # Definir os campos do formulário com os respectivos validadores
  fullname = StringField ('Fullname', validators=[validators.DataRequired (), validators.Length (min=3, max=50, message='O seu nome completo deve ter no máximo 50 caracteres, e no mínimo 3!')])
  email = EmailField ('Email', validators=[validators.DataRequired (), validators.Length (min=3, max=50, message='Digite um email válido, no mínimo 3 caracteres e no máximo 50!')])
  password = PasswordField('Senha', [
        validators.DataRequired(message='Insira uma senha!'),
        validators.Length (min=6, max=25, message='A senha deve ter no mínimo 6 digitos e no máximo 25!')
    ])
  confirm = PasswordField('Confirme a Senha', [
    validators.DataRequired(message='Insira a senha de confirmação!'),
    validators.EqualTo('password', message='As senhas devem ser iguais!'),
  ])
  color = StringField ('Cor', validators=[
    validators.DataRequired (message='Selecione uma cor na paleta de cores ou digite um código hexadecimal para sua cor preferida'), 
    validators.Length (min=7, max=7, message='O código hexadecimal deve conter exatamente 7 caracteres incluindo o #, por exemplo: #e62169'),
    validators.Regexp('^[0-9a-fA-F#]*$', message='O campo deve conter apenas caracteres hexadecimais, incluindo #.')], 
    default='#7c5dc5')
  age = IntegerField ('Idade', validators=[validators.DataRequired (), validators.NumberRange(min=13, message='A idade mínima para usar o Licse You é de 13 anos.')])

class UpdateAccForm (FlaskForm):

  fullname = StringField ('Fullname', validators=[validators.DataRequired (), validators.Length (min=3, max=50, message='O seu nome completo deve ter no máximo 50 caracteres, e no mínimo 3!')])

  color = StringField ('Cor', validators=[
    validators.DataRequired (message='Selecione uma cor na paleta de cores ou digite um código hexadecimal para sua cor preferida'), 
    validators.Length (min=7, max=7, message='O código hexadecimal deve conter exatamente 7 caracteres incluindo o #, por exemplo: #e62169'),
    validators.Regexp('^[0-9a-fA-F#]*$', message='O campo deve conter apenas caracteres hexadecimais, incluindo #.')], 
    default='#7c5dc5')
  age = IntegerField ('Idade', validators=[validators.DataRequired (), validators.NumberRange(min=13, message='A idade mínima para usar o Licse You é de 13 anos.')])