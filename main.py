from flask import Flask
from samenv import getenv
from flask_cors import CORS
from datetime import timedelta

def create_app():
  app = Flask(__name__)
  
  app.debug = getenv('LICSE_FLASK_DEBUG')
  app.config['FLASK_ENV'] = getenv('LICSE_FLASK_ENV')
  app.config['SECRET_KEY'] = getenv('LICSE_SECRET_KEY')
  app.permanent_session_lifetime = timedelta(days=14)  # Define o tempo de expiração para 7 dias
  from routes import views_routes, service_routes

  app.register_blueprint(views_routes.views_bp, url_prefix='/')
  app.register_blueprint(service_routes.services_bp, url_prefix='/services/')
  CORS(app)
  return app
