from flask import Flask,render_template,request,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,DateField,
                     SelectField,TextAreaField,RadioField,
                     SubmitField)
from wtforms.fields import TelField
from wtforms.validators import DataRequired


app=Flask(__name__)

app.config['SECRET_KEY']='mysecretkey'

class InfoForm(FlaskForm):
  breed=StringField('What breed are you?',validators=[DataRequired()])
  neutered=BooleanField("Have you been neutered?")
  mood=RadioField('Please choose your mood:',choices=[('mood_one','Happy'),('mood_two','Excited')])
  food_choice=SelectField('Pick you favorite food:',choices=[('chi','Chicken'),('bf','Beef'),('fish','Fish')])
  feedback=TextAreaField()
  submit=SubmitField('Submit')
  
  
  
  
@app.route('/',methods=['GET','POST'])
def index():
  form=InfoForm()
  
  if form.validate_on_submit():
    session['breed']=form.breed.data
    session['neutered']=form.neutered.data
    session['mood']=form.mood.data
    session['food_choice']=form.food_choice.data
    session['feedback']=form.feedback.data
    
    return redirect(url_for('thankyou'))
  
  return render_template('index.html',form=form)

@app.route('/thankyou')
def thankyou():
  return render_template('thankyou.html')

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'),404

if __name__=='__main__':
  app.run()