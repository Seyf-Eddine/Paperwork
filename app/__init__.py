from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

folder_path = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = f"""sqlite:///{os.path.join(folder_path, "paperwork.db")}"""
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from app import stores


def init_DB(decharge_store):
    if len(decharge_store.get_All()) > 0:
        pass
    else:
        db.drop_all()
        db.create_all()


decharge_store = stores.Dechargestore()

init_DB(decharge_store)

# from app import views
# from app import api
