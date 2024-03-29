from flask import Flask,render_template, request

app=Flask(__name__)


@app.route('/')
def index():
  return render_template('home.html')

@app.route('/report')
def report():
  username=request.args.get('username')
  lower_letter=False
  upper_letter=False
  num_end=False
  report=False

  lower_letter=any(c.islower() for c in username)
  upper_letter=any(c.isupper() for c in username)
  num_end=username[-1].isdigit()
  
  print(lower_letter,upper_letter,num_end)
  report=lower_letter and upper_letter and num_end
  
  return render_template('report.html',lower_letter=lower_letter,
                                      upper_letter=upper_letter,
                                      num_end=num_end,
                                      report=report,
                                      username=username)

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