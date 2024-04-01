from flask import Flask,render_template,redirect,session,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,RadioField,DateField,
                     SelectField,TextAreaField,SubmitField)
from wtforms.fields import TelField
from wtforms.validators import DataRequired
import dbconnection
db_conn=dbconnection.connectDB()

app=Flask(__name__,static_url_path='/static')

@app.route("/",methods=['GET'])
def index():
  print(db_conn)
  return 'its working'


if __name__=='__main__':
  app.run()
