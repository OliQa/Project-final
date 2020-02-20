from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DB_URI'))
db = SQLAlchemy(app)



from application import routes
