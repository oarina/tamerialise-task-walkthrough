import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

'''The __name__ is a built-in special variable that evaluates the name of the current module. 
If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value “__main__”. 
If this file is being imported from another module, __name__ will be set to the module’s name.

'''

db = SQLAlchemy(app) # instance of alchemy flask class

# below is how it's supposed to be
from taskmanager import routes # routes file will rely on above app and db to run, if we mention it above - we would get the circular error
