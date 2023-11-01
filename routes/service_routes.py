from flask import blueprints, redirect, render_template, send_file, request
import apiactions
import forms
import functions
services_bp = blueprints.Blueprint('services', __name__)

@services_bp.route('/sendvemail', methods=["GET"])
def sendvemail():
  return functions.sendvemail()

@services_bp.route('/deleteac', methods=["DELETE"])
def deleteac():
  return functions.deleteac()

@services_bp.route('/createchat', methods=["POST"])
def createchat():
  return functions.deleteac()

@services_bp.route('/deletechat', methods=["DELETE"])
def deletechat():
  return functions.deletechat()

@services_bp.route('/getchats', methods=['GET'])
def getchats():
  return functions.getchats()

@services_bp.route('/curchat', methods=['GET'])
def curchat():
  return functions.setcurchat()

@services_bp.route('/savemsg', methods=['POST'])
def savemsg():
  return functions.setcurchat()

@services_bp.route('/licseprompt', methods=['GET'])
def licseprompt():
  return functions.licseprompt()

@services_bp.route('/addmsg', methods=['POST'])
def addmsg():
  return functions.addmsg()