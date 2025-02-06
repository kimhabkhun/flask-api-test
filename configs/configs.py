from dotenv import load_dotenv
from os import getenv

try:
    load_dotenv(dotenv_path=".env.development")
    dbname = getenv("dbname","default")
    user = getenv("user","default")
    password = getenv("password","default")
    host = getenv("host","default")
    port = getenv("port","default")
except Exception as err:
    print("env error: ",err)
class Config():
    DEBUG = True
    DATABASE = {
        "dbname":dbname,
        "user":user,
        "password":password,
        "host":host,
        "port":port
    }
    # for db config
    class Db_Config():
        SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@localhost:5432/{dbname}'
