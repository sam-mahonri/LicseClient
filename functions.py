from flask import blueprints, redirect, render_template, send_file, request, session, flash
import apiactions
import forms

def signin():
  form = forms.LoginForm()

  if request.method == 'POST' and form.validate_on_submit():
    email = request.form.get('email', '')
    password = request.form.get('password', '')
    status = apiactions.log_in(email, password)

    if status == 'LICSE_SUCCESS': 
      return redirect('/')

    return render_template('signin.html', form=form, status=status)
  
  if apiactions.is_logged_in():
    return render_template('signin.html', form=form, status='LICSE_ALREADY')
  else:
    return render_template('signin.html', form=form, status='LICSE_NONE')
  

def signup():
  form = forms.RegisterForm()

  if request.method == 'POST' and form.validate_on_submit():
    email = request.form.get('email', '')
    fullname = request.form.get('fullname', '')
    password = request.form.get('password', '')
    color = request.form.get('color', '#7c5dc5')
    age = request.form.get('age', '13')

    status = apiactions.register(email, password, fullname, color, age)

    if status == 'LICSE_SUCCESS':
      status = apiactions.log_in(email, password)
      status = apiactions.send_email_ver()
    return render_template('signup.html', form=form, status=status)

  return render_template('signup.html', form=form, status='LICSE_NONE')

def ver_login():
  form_update_acc = forms.UpdateAccForm()
  resposta = apiactions.is_logged_in()
  email_verified = apiactions.verified_email()

  if request.method == 'POST':

    if form_update_acc.validate_on_submit():
      fullname = request.form.get('fullname', '')
      color = request.form.get('color', '#7c5dc5')
      age = request.form.get('age', '13')
      status = apiactions.updateac(fullname, age, color)
      if status == 'LICSE_SUCCESS':
        flash('Conta atualizada com êxito!', 'SUCCESS')
      else:
        flash('Falha ao atualizar os dados da conta!', 'ERROR')

      return redirect('/')
    else:

      return render_template('home.html', session=session, emailver=email_verified, form=form_update_acc, form_update_acc=form_update_acc, opened='acUpdate')
  if not resposta:
    return redirect('/signin')
  else:
    return render_template('home.html', session=session, emailver=email_verified, form=form_update_acc, form_update_acc=form_update_acc)
  
def sendvemail():
  result = apiactions.send_email_ver()
  return result

def deleteac():
  result = apiactions.deleteac()
  return result
