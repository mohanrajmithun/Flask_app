from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import path
from flask_login import LoginManager

from sqlalchemy import URL

import urllib


db = SQLAlchemy()
DB_NAME = "Website"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MY SUPER SECRET KEY'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:mysqlcar0596@DESKTOP-VOE2SHH/Website'
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://Mithun_sql:password123@DESKTOP-VOE2SHH/Website?driver=ODBC Driver 17 for SQL Server"
    # url_object = URL.create(
    # "mssql+pyodbc",
    # username="Mithun_sql",
    # password="password123",  # plain (unescaped) text
    # host="DESKTOP-VOE2SHH",
    # database="Website",
    # )

    # app.config['SQLALCHEMY_BINDS'] = {'url':url_object}


  


    # db.create_engine(url_object)
    # SERVER = 'DESKTOP-VOE2SHH'
    # DATABASE = 'Website'

    # USERNAME = 'Mithun_sql'
    # PASSWORD = 'password123'
    # app.config["SQLALCHEMY_DATABASE_URI"] = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'


    db.init_app(app)



    from .auth import auth
    from .views import views


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_db(app)

    from .models import User, Note


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_db(app):

        with app.app_context():
            db.create_all()
        print('database created!')

