from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from models import db, User, Index, socialdash_followers

class ContactForm(Form):
    name = TextField("Name",  [validators.Required("Please enter your name.")])
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    subject = TextField("Subject",  [validators.Required("Please enter a subject.")])
    message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
    submit = SubmitField("Send")

class SignupForm(Form):
    
    firstname = TextField("Index1",  [validators.Required("Please enter your first name.")])
    lastname = TextField("Index2",  [validators.Required("Please enter your last name.")])
    email = TextField("Index3",  [validators.Required("Please enter your email address.")])
    password = PasswordField('Index4', [validators.Required("Please enter a password.")])
    submit = SubmitField("Create")


    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
         
        user = User.query.filter_by(email = self.email.data.lower()).first()
        if user:
          self.email.errors.append("That email is already taken")
          return False
        else:
          return True

class IndexForm(Form):
    
    index1 = TextField("Index1",  [validators.Required("Please enter index1 .")])
    index2= TextField("Index2",  [validators.Required("Please enter index2 .")])
    index3 = TextField('Index3', [validators.Required("Please enter index3 .")])
    index4 = TextField('Index4', [validators.Required("Please enter index4 .")])
    submit= SubmitField("Insert indexes")

class SigninForm(Form):

  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.Required("Please enter a password.")])
  submit = SubmitField("Sign In")
   
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user and user.check_password(self.password.data):
      return True
    else:
      self.email.errors.append("Invalid e-mail or password")
      return False

