from flask import Flask
from flask_apscheduler import APScheduler

scheduler = APScheduler()

def create_app():
    app = Flask(__name__)
    scheduler.init_app(app)
    return app