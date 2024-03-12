from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/template_variable')
def templateVarible():
  name="khadar"
  letters=list(name)
  puppy_dict={'name':'Ruffiy'}
  
  return render_template('temp_variable.html',name=name,
                         letters=letters,
                         puppy_dict=puppy_dict)

@app.route('/controlstatements')
def controlStatements():
  users=['khadar','sayyad','basha','ajay','ninja']
  
  return render_template('controlstatements.html',users=users)

if __name__=='__main__':
  app.run()