from flask import Flask, redirect, url_for, request
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security, current_user



app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)


