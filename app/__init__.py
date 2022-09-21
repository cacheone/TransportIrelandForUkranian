from flask import Flask
from config import Config
from .models import db
from .views import mainroute


app = Flask(__name__)
config = Config()
app.config.from_object(config)
db.init_app(app)
app.register_blueprint(mainroute)


