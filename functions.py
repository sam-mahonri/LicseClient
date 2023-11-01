from flask import blueprints, redirect, render_template, send_file, request, session, flash, url_for, jsonify
import apiactions
import forms

def signin():
  form = forms.LoginForm()

  if request.method == 'POST' and form.validate_on_submit():
    email = request.form.get('email', '')
    password = request.form.get('password', '')

    if request.form.get('keeplogged', 'off') == 'on':
      session['keeplogged'] = request.form.get('keeplogged', 'off')
      session['email'] = email
      session['password'] = password
      session.permanent = True
    else:
      session.permanent = False
      session['keeplogged'] = 'off'
      session['email'] = ''
      session['password'] = ''
    
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
  form_create_chat = forms.CreateChat()
  resposta = apiactions.is_logged_in()
  email_verified = apiactions.verified_email()

  if request.method == 'POST':
    if 'createChatBt' in request.form:
      if form_create_chat.validate_on_submit():
        title = request.form.get('title', '')
        status = apiactions.create_chat(title)
        if status == 'LICSE_SUCCESS':
          apiactions.is_logged_in()
          form_create_chat = forms.CreateChat()
          flash('Conversa criada com êxito!', 'SUCCESS')
          session['flow_opened'] = 'chatList'
          return redirect('/')
        else:
          flash('Falha ao criar conversa! Tente: Fazer login novamente ou tentar mais tarde.', 'ERROR')
          session['flow_opened'] = ''
          return render_template('home.html', session=session, emailver=email_verified, form=form_update_acc, form_update_acc=form_update_acc, form_create_chat=form_create_chat, opened='chatList')
      
    elif 'updateAccountBt' in request.form:
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
        return render_template('home.html', session=session, emailver=email_verified, form=form_update_acc, form_update_acc=form_update_acc, form_create_chat=form_create_chat, opened='acUpdate')
    
  if not resposta:
    if session.get('keeplogged', 'off') == 'on':

      status = apiactions.log_in(session.get('email', ''), session.get('password', ''))

      if status == 'LICSE_SUCCESS': 
        return redirect('/')

    return redirect('/signin')
  else:
    return render_template('home.html', session=session, emailver=email_verified, form_update_acc=form_update_acc, form_create_chat=form_create_chat)
  
def sendvemail():
  result = apiactions.send_email_ver()
  return result

def deleteac():
  result = apiactions.deleteac()
  return result

def deletechat():
  result = apiactions.delete_chat(request.args.get('chatId'))
  return result

def getchats():
  print(session.get('chats', {}))
  return jsonify(session.get('chats', {}))

def setcurchat():
  session['current_chat'] = request.args.get('chatId')
  return 'OK'

def licseprompt():
  prompt = request.args.get('prompt')
  pType = request.args.get('type')
  result = apiactions.licse_prompt(prompt=prompt, pType=pType)
  return result

def addmsg():
  msg = request.args.get('msg')
  sender = request.args.get('sender')
  chatid = request.args.get('chatId')
  result = apiactions.addmsg(msg=msg, sender=sender, chatId=chatid)
  return result