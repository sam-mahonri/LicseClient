from apiendpoints import *
import requests
from flask import session
import json
import os

headers = {'Content-Type': 'application/json'}

def is_logged_in():
    if 'userToken' in session and "userId" in session:
        ##### RECARREGAR DADOS DO USUÁRIO SEMPRE QUE A PÁGINA ABRIR #####
        if 'LICSE_ERROR' in get_user_info(): return False 
        else: return True
        #return True
    else:
        return False

def register(email, password, fullname, color, age):
    url = LICSE_REGISTER


    data = {
        "email": email,
        "password": password,
        "fullName": fullname,
        "favColor": color,
        "age": age
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, verify=LICSE_VERIFY_SSL, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        session['userToken'] = response_data['token']
        session['userId'] = response_data['userId']
        return 'LICSE_SUCCESS'
    else:
        session['expired'] = True
        log_out()
        return 'LICSE_ERROR'

def log_in(email, password):
    url = LICSE_LOGIN
    data = {
        "email": email,
        "password": password
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, verify=LICSE_VERIFY_SSL, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        session['userToken'] = response_data['token']
        session['userId'] = response_data['userId']
        get_user_info()
        return 'LICSE_SUCCESS'
    else:
        session['expired'] = True
        log_out()
        return 'LICSE_ERROR'

def log_out():
        if 'userToken' in session: session.pop('userToken')
        if 'userId' in session: session.pop('userId')
        if 'fullName' in session: session.pop('fullName')
        if 'favColor' in session: session.pop('favColor')
        if 'points' in session: session.pop('points')
        if 'redflags' in session: session.pop('redflags')

def send_email_ver():
    url = LICSE_SENDEMAIL_VER

    if not 'userToken' in session and "userId" in session:
        return 'LICSE_ERROR'
    
    data = {
        "token": session.get('userToken', ''),
        "userId": session.get('userId', '')
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, verify=LICSE_VERIFY_SSL, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        return 'LICSE_SUCCESS'
    else:
        session['expired'] = True
        log_out()
        
        return 'LICSE_ERROR'
    
def get_user_info():
    url = LICSE_GET_CURRENT_USER

    if not 'userToken' in session and "userId" in session:
        return {'LICSE_ERROR':'Ocorreu um erro'}
    
    data = {
        "token": session.get('userToken', ''),
        "userId": session.get('userId', '')
    }

    json_data = json.dumps(data)

    response = requests.get(url, data=json_data, verify=LICSE_VERIFY_SSL, headers=headers)

    if response.status_code == 200:
        response_data = response.json()['gotData']

        if response_data is None:
            log_out()
            return {'LICSE_ERROR':'Os dados não existem mais'}


        session['fullName'] = response_data.get('fullName', '')
        session['favColor'] = response_data.get('favColor', '')
        session['age'] = response_data.get('age', '')
        session['points'] = response_data.get('points', '')
        session['redflags'] = response_data.get('redflags', '')
        session['chats'] = response_data.get('chats', {})
        session['expired'] = False
        return response_data
    else:
        log_out()
        
        session['fullName'] = ''
        session['favColor'] = ''
        session['age'] = ''
        session['points'] = ''
        session['redflags'] = ''
        session['chats'] = {}
        session['expired'] = True
        return {'LICSE_ERROR':'Ocorreu um erro'}
    
def verified_email():
    url = LICSE_VER_EMAIL
    if not 'userToken' in session and "userId" in session:
        return False
    
    data = {
        "token": session.get('userToken', ''),
        "userId": session.get('userId', '')
    }

    json_data = json.dumps(data)
    response = requests.post(url, data=json_data, verify=LICSE_VERIFY_SSL, headers=headers)

    if response.status_code == 200:

        outp = False
        if response.text == "true\n": outp = True
        else: outp = False
        return outp
    else:
        session['expired'] = True
        if session.get('keeplogged', 'off') == 'on':
            log_in(session.get('email', ''), session.get('password', ''))
            verified_email()
        else:
            return False

def deleteac():
    url = LICSE_DELETE_AC

    if not 'userToken' in session and "userId" in session:
        return 'LICSE_ERROR'
    
    data = {
        "token": session.get('userToken', ''),
        "userId": session.get('userId', '')
    }

    json_data = json.dumps(data)

    response = requests.delete(url, data=json_data, verify=LICSE_VERIFY_SSL, headers=headers)
    if response.status_code == 200:
        json_out = response.json()
        if "licseError" in json_out:
            if json_out['licseError'] == 'SUCCESS_DELETE_USER_REGISTER': return 'LICSE_SUCCESS'
            elif json_out['licseError'] == 'ERROR_DELETE_USER_REGISTER': return 'LICSE_ERROR'
    else:
        session['expired'] = True
        if session.get('keeplogged', 'off') == 'on':
            log_in(session.get('email', ''), session.get('password', ''))
            verified_email()
        else:
            return 'LICSE_ERROR'
    
def updateac(fullname, age, color):
    url = LICSE_UPDATE_AC

    if not 'userToken' in session and "userId" in session:
        return 'LICSE_ERROR'
    
    data = {
        "data": {
            "fullName": fullname,
            "age": age,
            "favColor": color
        },
        "token": session.get('userToken', ''),
        "userId": session.get('userId', '')
    }

    json_data = json.dumps(data)

    response = requests.put(url, data=json_data, verify=LICSE_VERIFY_SSL, headers=headers)

    if response.status_code == 200:
        json_out = response.json()
        
        if "licseError" in json_out:
            if json_out['licseError'] == 'SUCCESS_USER_UPDATED':
                session['fullName'] = fullname
                session['favColor'] = color
                session['age'] = age
                return 'LICSE_SUCCESS'
            elif json_out['licseError'] == 'ERROR_USER_UPDATED':
                session['expired'] = True
                return 'LICSE_ERROR'
    else:
        session['expired'] = True
        if session.get('keeplogged', 'off') == 'on':
            log_in(session.get('email', ''), session.get('password', ''))
            updateac()
        else:
            return 'LICSE_ERROR'

def create_chat(title):
    url = LICSE_CREATE_CHAT

    if not 'userToken' in session and "userId" in session:
        return 'LICSE_ERROR'
    
    data = {
        "title": title,
        "token": session.get('userToken', ''),
        "userId": session.get('userId', '')
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, verify=LICSE_VERIFY_SSL, headers=headers)

    if response.status_code == 200:
        json_out = response.json()
        
        if "licseError" in json_out:
            if json_out['licseError'] == 'SUCCESS_CREATE_CHAT':
                session['current_chat'] = json_out.get('chatId', 'noId_FATAL')
                return 'LICSE_SUCCESS'
            elif json_out['licseError'] == 'ERROR_CREATE_CHAT':
                session['expired'] = True
                session['current_chat'] = ''
                return 'LICSE_ERROR'
    else:
        session['expired'] = True
        if session.get('keeplogged', 'off') == 'on':
            log_in(session.get('email', ''), session.get('password', ''))
            create_chat()
        else:
            return 'LICSE_ERROR'

def delete_chat(chatId):
    url = LICSE_DELETE_CHAT

    if not 'userToken' in session and "userId" in session:
        return 'LICSE_ERROR'
    
    data = {
        "chatId": chatId,
        "token": session.get('userToken', ''),
        "userId": session.get('userId', '')
    }

    json_data = json.dumps(data)

    response = requests.delete(url, data=json_data, verify=LICSE_VERIFY_SSL, headers=headers)

    if response.status_code == 200:
        json_out = response.json()
        
        if "licseError" in json_out:
            if json_out['licseError'] == 'SUCCESS_CHAT_DELETE':
                return 'LICSE_SUCCESS'
            elif json_out['licseError'] == 'ERROR_CHAT_DELETE':
                session['expired'] = True
                return 'LICSE_ERROR'
    else:
        session['expired'] = True
        log_out()
        return 'LICSE_ERROR'

def licse_prompt(prompt, pType="WEB"):
    url = LICSE_PROMPT

    if not 'userToken' in session and "userId" in session:
        return 'LICSE_ERROR'
    
    data = {
        "prompt": prompt,
        "type": pType,
        "token": session.get('userToken', ''),
        "userId": session.get('userId', '')
    }

    json_data = json.dumps(data)

    response = requests.get(url, data=json_data, verify=LICSE_VERIFY_SSL, headers=headers)

    if response.status_code == 200:
        json_out = response.json()
        
        if "licseError" in json_out:
            print(json_out['licseError'])
            return 'LICSE_ERROR'

        return json_out
    else:
        session['expired'] = True
        log_out()
        return 'LICSE_ERROR'
    
def addmsg(msg, sender, chatId):
    url = LICSE_ADDMSG_CHAT

    if not 'userToken' in session and "userId" in session:
        return 'LICSE_ERROR'
    
    data = {
        "sender":sender,
        "message":msg,
        "chatId": chatId,
        "token": session.get('userToken', ''),
        "userId": session.get('userId', '')
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, verify=LICSE_VERIFY_SSL, headers=headers)

    if response.status_code == 200:
        json_out = response.json()
        
        if "licseError" in json_out:
            if json_out['licseError'] == 'SUCCESS_MSG_SAVED':
                return 'LICSE_SUCCESS'
            elif json_out['licseError'] == 'ERROR_MSG_SAVED':
                session['expired'] = True
                return 'LICSE_ERROR'
    else:
        session['expired'] = True
        log_out()
        return 'LICSE_ERROR'