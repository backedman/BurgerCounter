# 3rd-party packages
from flask import Flask, render_template, request, redirect, url_for
from flask_mongoengine import MongoEngine
from flask_login import (
    LoginManager,
    current_user,
    login_user,
    logout_user,
    login_required,
)
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename


# stdlib
from datetime import datetime
import os

#local
from .calorie_api import NutritionNinjaAPI
NNA_KEY = 'Uv9UoG21C7OMpfjhmJTSeA==U77gFRDxSkovYvgz'

db = MongoEngine()
login_manager = LoginManager()
bcrypt = Bcrypt()
calorie_count_api = NutritionNinjaAPI(NNA_KEY)

from .users.routes import users
from .authentication.routes import authentication




def custom_404(e):
    return render_template("404.html"), 404


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_pyfile("config.py", silent=False)
    if test_config is not None:
        app.config.update(test_config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(users)
    app.register_blueprint(authentication)
    app.register_error_handler(404, custom_404)

    login_manager.login_view = "authentication.login"

    return app
