from flask import Flask,render_template,redirect,session,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,RadioField,DateField,
                     SelectField,TextAreaField,SubmitField)
from wtforms.fields import TelField
from wtforms.validators import DataRequired
import dbconnection
db_conn=dbconnection.connectDB()

app=Flask(__name__,template_folder='templates',static_url_path='/static')

@app.route("/",methods=['GET'])
def index():
  return render_template("index.html")

@app.route("/register",methods=['GET'])
def register():
  return render_template("register.html")

@app.route("/forgotpwd",methods=['GET'])
def forgotpwd():
  return render_template("forgotpassword.html")

@app.route("/dashboard",methods=['GET'])
def dashboard():
  return render_template("dashboard.html")

@app.route("/users",methods=['GET'])
def users():
  return render_template("users.html")

@app.route("/adduser",methods=['GET'])
def adduser():
  return render_template("add_user.html")

@app.route("/logout",methods=['GET'])
def logout():
  return redirect('/')


if __name__=='__main__':
  app.run()
