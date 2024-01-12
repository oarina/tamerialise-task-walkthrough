import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env

app = flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQALCHEMY_DATABASE_URI"] = os.environget("DB_URL")

db = SQLAlchemy(app)

from taskmanager import routes 
