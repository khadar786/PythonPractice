from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
  users=['khadar','sayyad','basha','ajay','ninja']
  return render_template('home.html',users=users)

@app.route('/view/<title>')
def viewDetails(title):
  return render_template('view.html',title=title)

if __name__=='__main__':
  app.run()