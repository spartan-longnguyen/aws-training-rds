from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .models import User  # Import your models from models.py file

__all__ = ['User']
