from flask import Flask, session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool, QueuePool
import os
from dotenv import load_dotenv

# load_dotenv('environment/local.env')

app = Flask(__name__)


app.engine = None
app.session=None


@app.before_request
def before_request():

    if not app.engine:
        app.engine = create_engine("mysql+pymysql://root:Neo#12345@localhost:3306/mytestdb")
        app.session = scoped_session(sessionmaker(bind=app.engine))



Base = declarative_base()

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    city = Column(String)

@app.route('/', methods=['GET'])
def home():
    datas = app.session.query(User).all()
    print([data.name for data in datas])
    return "Sucess" + str([(data.name, data.age, data.city )for data in datas])

@app.teardown_appcontext
def shutdown(exception=None):
    if app.session is not None:
       app.session.remove()

if __name__== "__main__":
    app.run(debug=True)

