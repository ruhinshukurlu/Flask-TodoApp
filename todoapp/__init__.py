from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fct5hvxkmJkyKZfePxZ3EAW'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345@localhost:3307/todo_db' 
db = SQLAlchemy(app)


bcrypt = Bcrypt(app)
from todoapp import routs