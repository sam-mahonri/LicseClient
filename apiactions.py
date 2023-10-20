from apiendpoints import *
import requests
from flask import session
import json
import os

headers = {'Content-Type': 'application/json'}

def is_logged_in():
    if 'userToken' in session and "userId" in session:
        if 'LICSE_ERROR' in get_user_info(): return False 
        else: return True
    else:
        return False

def register(email, password, fullname, color, age):
    url = LICSE_REGISTER

    # Defina os dados do corpo da solicitação (email e senha)
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
        log_out()
        return 'LICSE_ERROR'

def log_in(email, password):
    url = LICSE_LOGIN

    # Defina os dados do corpo da solicitação (email e senha)
    data = {
        "email": email,
        "password": password
    }

    json_data = json.dumps(data)

    # Faça a solicitação POST com os dados
    response = requests.post(url, data=json_data, verify=LICSE_VERIFY_SSL, headers=headers)

    # Verifique se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # A solicitação foi bem-sucedida, e você pode processar a resposta
        response_data = response.json()  # Se a resposta for em formato JSON
        session['userToken'] = response_data['token']
        session['userId'] = response_data['userId']
        get_user_info()
        return 'LICSE_SUCCESS'
    else:
        # A solicitação falhou, e você pode lidar com erros
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

    # Defina os dados do corpo da solicitação (email e senha)

    if not 'userToken' in session and "userId" in session:
        return 'LICSE_ERROR'
    
    data = {
        "token": session['userToken'],
        "userId": session['userId']
    }

    json_data = json.dumps(data)

    # Faça a solicitação POST com os dados
    response = requests.post(url, data=json_data, verify=LICSE_VERIFY_SSL, headers=headers)

    # Verifique se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # A solicitação foi bem-sucedida, e você pode processar a resposta
        response_data = response.json()
        return 'LICSE_SUCCESS'
    else:
        log_out()
        
        return 'LICSE_ERROR'
    
def get_user_info():
    url = LICSE_GET_CURRENT_USER

    # Defina os dados do corpo da solicitação (email e senha)

    if not 'userToken' in session and "userId" in session:
        return {'LICSE_ERROR':'Ocorreu um erro'}
    
    data = {
        "token": session['userToken'],
        "userId": session['userId']
    }

    json_data = json.dumps(data)

    response = requests.get(url, data=json_data, verify=LICSE_VERIFY_SSL, headers=headers)

    if response.status_code == 200:
        response_data = response.json()['gotData']

        if response_data is None:
            log_out()
            return {'LICSE_ERROR':'Os dados não existem mais'}

        print(response_data)

        session['fullName'] = response_data.get('fullName', '')
        session['favColor'] = response_data.get('favColor', '')
        session['age'] = response_data.get('age', '')
        session['points'] = response_data.get('points', '')
        session['redflags'] = response_data.get('redflags', '')
        return response_data
    else:
        log_out()
        
        session['fullName'] = ''
        session['favColor'] = ''
        session['age'] = ''
        session['points'] = ''
        session['redflags'] = ''

        return {'LICSE_ERROR':'Ocorreu um erro'}