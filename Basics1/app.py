from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
  return '<h1>Hello Puppy</h1>'

@app.route('/information')
def info():
  return "<h1>Puppies are cute!</h1>"

@app.route('/puppy/<name>')
def puppy(name):
  #return "<h1>Upper case : {}</h1>".format(name.upper())
  return "<h1>Upper case : {}</h1>".format(name)

@app.route('/puppy_name/<name>')
def puppylatin(name):
  pupname=''
  
  if name[-1]=='y':
    pupname=name[:-1]+'iful'
  else:
    pupname=name+'y'

  return "<h1>Your puppy latin name is : {}</h1>".format(pupname)


if __name__ == '__main__':
  ##app.run()
  app.run(debug=True)