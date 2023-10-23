import os
from dotenv import load_dotenv

load_dotenv()

"""
    Archivo que funciona de interfaz entre las variables de entorno y la aplicación
"""
db_user = os.getenv("MYSQL_USER")
db_password = os.getenv("MYSQL_PASSWORD")
db_host = os.getenv("MYSQL_HOST")
db_name = os.getenv("MYSQL_DB")
db_port = os.getenv("MYSQL_PORT")