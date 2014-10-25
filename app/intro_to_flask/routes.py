from intro_to_flask import app
from flask import render_template, request, flash, session, url_for, redirect
from forms import ContactForm,SignupForm, SigninForm, IndexForm
from flask.ext.mail import Message, Mail
import models
from models import db,User,Index,socialdash_followers
import os
from flask import url_for


mail = Mail()
# app = Flask(__name__)

app.secret_key = 'development key' 

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'jennxf.ng@gmail.com'
app.config["MAIL_PASSWORD"] = 'Jennxf1989'
 
mail.init_app(app)     
 
@app.route('/')
def home():
   
  return render_template('home.html')


@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
  
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='jennxf.ng@gmail.com', recipients=['jennxf.ng@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return render_template('contact.html', success=True)
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

# @app.route('/testdb')
# def testdb():
#   if db.session.query("1").from_statement("SELECT 1").all():
#     return 'It works.'
#   else:
#     return 'Something is broken.'

@app.route('/index', methods=['GET','POST'])
def index():
  form2 = IndexForm()

  # if 'email' in session:
  #   return redirect(url_for('profile'))
   
  if request.method == 'POST':
      
      newindex = Index(form2.index1.data, form2.index2.data, form2.index3.data, form2.index4.data)
      db.session.add(newindex)
      db.session.commit() 
      print "see something?"
      return redirect(url_for('profile'))

  elif request.method == 'GET':
      return render_template('index.html', form=form2)

      


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()
       
      session['email'] = newuser.email
      print "yoyo"
      return redirect(url_for('profile'))
   
  elif request.method == 'GET':
    return render_template('signup.html', form=form)


@app.route('/profile')
def profile():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
 
  user = User.query.filter_by(email = session['email']).first()
 
  if user is None:
    return redirect(url_for('signin'))
  else:
    return render_template('profile.html', indexes_new=Index.query.all(), result=socialdash_followers().get_followers())
    # users=User.query.order_by(User.firstname.desc()).all()
@app.route('/signin', methods=['GET', 'POST'])
def signin():
  form = SigninForm()

  if 'email' in session:
    return redirect(url_for('profile'))
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signin.html', form=form)
    else:
      session['email'] = form.email.data
      return redirect(url_for('profile'))
                 
  elif request.method == 'GET':
    return render_template('signin.html', form=form)

@app.route('/signout')
def signout():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
     
  session.pop('email', None)
  return redirect(url_for('home'))

@app.route('/d3')
def d3():
  return render_template('d3.html')


# #let's create ourselves a new route
# @app.route('/data/text.json')
# def data_proxy():
#     # send_static_file will guess the correct MIME type
#   return app.send_static_file("/data/text.json")


 
if __name__ == '__main__':
  app.run(debug=True)
  url_for('static', filename='uservoice4.json')

