from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import *
from datetime import date
import os


from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "tests"
jwt = JWTManager(app)
CORS(app)
path = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(path, "stock.db")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+arquivobd
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)