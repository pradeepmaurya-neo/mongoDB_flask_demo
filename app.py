from flask import Flask, session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool, QueuePool
import os
from dotenv import load_dotenv

load_dotenv('environment/local.env')

app = Flask(__name__)

# expmerimet #1

# engine = create_engine("mysql+pymysql://root:Neo#12345@localhost:3306/mytestdb")
# engine = create_engine("mysql+pymysql://root:Neo#12345@localhost:3306/mytestdb", poolclass=NullPool)
# engine = create_engine("mysql+pymysql://root:Neo#12345@localhost:3306/mytestdb", pool_size=5, max_overflow=0, pool_pre_ping=True)
# engine = create_engine("mysql+pymysql://root:Neo#12345@localhost:3306/mytestdb", poolclass=QueuePool, echo=True)


#pass
# engine = create_engine("mysql+pymysql://root:Neo#12345@localhost:3306/mytestdb", pool_size=5, max_overflow=10, pool_pre_ping=True, pool_recycle=30, echo=True, pool_timeout=30)

# print("____________________===============", os.environ.get('HELLO'))
# app.engine = None
# app.session=None


# @app.before_request
# def before_request():

#     app.engine = create_engine("mysql+pymysql://root:Neo#12345@localhost:3306/mytestdb"
#         # pool_size=5,
#         # max_overflow=10,
#         # pool_pre_ping=True,
#         # pool_recycle=30,
#         # echo=True,
#         # pool_timeout=30,
#         # poolclass=NullPool,
#         # connect_args={'connect_timeout': 10},
#         # use_fifo=True
#     )
#     app.session = scoped_session(sessionmaker(bind=app.engine))
    # return 'session'
# create_engine(db_url, connect_args={'connect_timeout': 10})

# pool = QueuePool(engine, pool_size=10, max_overflow=0, timeout=200)
# def run_in_process(some_data_record):

#     with engine.connect() as conn:
#         conn.execute(text("..."))
# print(engine.status())
# def initializer():
#     """ensure the parent proc's database connections are not touched
#        in the new connection pool"""
#     engine.dispose(close=False)

# with Pool(10, initializer=initializer) as p:
#     p.map(run_in_process, data)


# experiment #2

# connection_eng = create_engine("mysql+pymysql://root:Neo#12345@localhost:3306/mytestdb")
# conx_pool = QueuePool(connection_eng, pool_size=2, max_overflow=2)
# engine = conx_pool.connect()



# app.config["SQLALCHEMY_POOL_SIZE"] = 5
# app.config["SQLALCHEMY_MAX_OVERFLOW"] = 10
# app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30


# app.session=None
session = scoped_session(sessionmaker(bind=engine))
# session = Session()

Base = declarative_base()



class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    city = Column(String)

@app.route('/', methods=['GET'])
def home():
    datas = session.query(User).all()
    print([data.name for data in datas])
    return "Sucess" + str([(data.name, data.age, data.city )for data in datas])


# @app.teardown_appcontext
# def shutdown(exception=None):
#     if session is not None:
#         session.remove()


# @app.teardown_appcontext
# def shutdown(exception=None):
#     if app.session is not None:
#         app.session.dispose()
    
    # if Exception:
    # session.rollback()
    # session.remove()
# session.remove()
# eng_obj = app.engine


# print(app.engine)

# @app.after_request
# def eng_shut(response):
#     print("2222222222222222222222222222", app.engine)
#     # app.engine.close
#     app.session.remove()
#     print("33333333333333333333", app.engine)
#     return response

if __name__== "__main__":
    app.run(debug=True)