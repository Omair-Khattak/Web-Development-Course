import os

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql6477802:6f3jE8CyVA@sql6.freemysqlhosting.net:3306/sql6477802'

from Api import models
from Api import views
