from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '6deea3b3503ffd897ceeeb5159b8b615' # used to verify authenticity of user login.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/colewhaley/basketballDB/SQLite DB/Hoops.db'
db = SQLAlchemy(app)

from basketballDB import routes