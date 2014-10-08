from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
 
db = SQLAlchemy()

# class NetbaseTopics:
#   def get_topics(self):
#     engine = create_engine('mysql://xng2:hello@localhost/netbase')
#     connection = engine.connect()
# #     return connection.execute("select * from topics")

class socialdash_followers:
  def get_followers(self):
    engine = create_engine('mysql://xng2:hello@localhost/socialdash')
    connection = engine.connect()
    print "connected!"
    rows=connection.execute("select * from followers2")
    result_list=[]
    for row in rows:
      result = {}
      result['id']=row['id']
      result['date']=row['date'] 
      result['FB_Followers']=row['FB_Followers'] 
      result['TW_Followers']=row['TW_Followers'] 
      result['Youtube_Followers']= row['Youtube_Followers'] 
      result['G_Plus_Followers']=row['G_Plus_Followers'] 
      result['sum_fans']=row['sum_fans'] 
      result['speed_of_growth']=row['speed_of_growth']
      result['FB_Fan_Growth_Speed']= row['FB_Fan_Growth_Speed']
      result['TW_Fan_Growth_Speed']= row['TW_Fan_Growth_Speed']
      result['Fan_Growth_index']= row['Fan_Growth_index']
      result_list.append(result)
    return result_list
    

class Index(db.Model):
  __tablename__ = 'indexes_new'
  iid = db.Column(db.Integer, primary_key = True, autoincrement = True)
  index1 = db.Column(db.Float)
  index2 = db.Column(db.Float)
  index3 = db.Column(db.Float)
  index4 = db.Column(db.Float)
   
  def __init__(self, index1, index2, index3, index4):
    self.index1=index1
    self.index2=index2
    self.index3=index3
    self.index4=index4

class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))
   
  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)
     
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)
   
  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)




