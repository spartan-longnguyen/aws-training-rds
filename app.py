# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
#
# app = Flask(__name__)
#
# # Configure the database connection URL for Amazon RDS
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@longnguyen-db.ci1xxxcuy6pi.ap-southeast-1.rds.amazonaws.com:5432/postgres'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# # Initialize SQLAlchemy and Migrate
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
#
# # Define your models below
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
#     def __repr__(self):
#         return f'<User {self.username}>'

from flask import Flask
from models import db

app = Flask(__name__)

# Configure the database connection URL for Amazon RDS
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@longnguyen-db.ci1xxxcuy6pi.ap-southeast-1.rds.amazonaws.com:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

# ... define routes and other application logic
