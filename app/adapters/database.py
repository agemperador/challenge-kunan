
from flask_sqlalchemy import SQLAlchemy
from app.config.config import db_user, db_password, db_host, db_name, db_port


## Modularizo la base de datos en su propia clase para aislar sqlalchemy
class Database ():

    def __init__(self):
        ##constructor de la base de datos
        self.db  = SQLAlchemy()
        self.db_url = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}'
        self.db_key = 'SQLALCHEMY_DATABASE_URI'

    #método de inicializacion
    def init_app(self, app):
        self.db.init_app(app)

    def save_element(self, element):
        self.db.session.add(element)
        self.db.session.commit()

database = Database()

