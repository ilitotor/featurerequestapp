from flask import Flask, render_template, request
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)

    from app import routes
    routes.load(app)

    return app