from flask import Flask,render_template,flash,request,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField)
from wtforms.fields import TelField
from wtforms.validators import DataRequired


app=Flask(__name__)

app.config['SECRET_KEY']='mysecretkey'

class SimpleForm(FlaskForm):
  submit=SubmitField('Clicke Me.')
  
  
  
  
@app.route('/',methods=['GET','POST'])
def index():
  form=SimpleForm()
  
  if form.validate_on_submit():
    flash('You just clicked the button!')
    return redirect(url_for('index'))
  
  return render_template('index.html',form=form)

@app.route('/thankyou')
def thankyou():
  return render_template('thankyou.html')

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'),404

if __name__=='__main__':
  app.run()