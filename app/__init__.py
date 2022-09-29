from flask import Flask
from config import Config
from .models import db
from .views import mainroute
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config.from_object(Config())
db.init_app(app)
app.register_blueprint(mainroute)
csrf = CSRFProtect()
csrf.init_app(app)
