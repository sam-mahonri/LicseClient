from flask import blueprints, redirect, render_template, send_file, request
import apiactions
import forms
import functions
services_bp = blueprints.Blueprint('services', __name__)

@services_bp.route('/sendvemail', methods=["GET"])
def sendvemail():
  return functions.sendvemail()

