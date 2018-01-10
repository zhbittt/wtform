from flask import Flask
from .config import config
from flask_session import Session
app = Flask(__name__,static_folder='static', template_folder='templates')

app.config.from_object(config["default"])

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
Session(app)