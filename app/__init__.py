from flask import Flask
from config import Config
from .models import db


app = Flask(__name__)
from app import views


config = Config()
app.config.from_object(config)
db.init_app(app)
