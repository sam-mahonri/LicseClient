from flask import blueprints, redirect, render_template, send_file, request
import apiactions
import forms
import functions
views_bp = blueprints.Blueprint('views', __name__)

@views_bp.route('/', methods=["GET", "POST"])
def index():
  return functions.ver_login()

@views_bp.route('/signin', methods=['GET', 'POST'])
def signin():
  return functions.signin()

@views_bp.route('/signup', methods=["GET", "POST"])
def signup():
  return functions.signup()

@views_bp.route('/logout')
def logout():
   apiactions.log_out()
   return redirect('/signin')

@views_bp.route('/favicon.ico')
def favicon():
  return send_file('./static/source/favicon.ico')



