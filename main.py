from flask import Flask
from samenv import getenv

def create_app():
  app = Flask(__name__)

  app.debug = getenv('LICSE_FLASK_DEBUG')
  app.config['FLASK_ENV'] = getenv('LICSE_FLASK_ENV')
  app.config['SECRET_KEY'] = getenv('LICSE_SECRET_KEY')
  
  from routes import views_bp

  app.register_blueprint(views_bp, url_prefix='/')
  
  return app
