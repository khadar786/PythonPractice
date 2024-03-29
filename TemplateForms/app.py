from flask import Flask,render_template, request

app=Flask(__name__)


@app.route('/')
def index():
  return render_template('home.html')

@app.route('/sign_up')
def sign_up():
  return render_template('signup.html')

@app.route('/thank_you')
def thank_you():
  first=request.args.get('first')
  last=request.args.get('last')
  return render_template('thank_you.html',first=first,last=last)

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'),404

if __name__=='__main__':
  app.run()