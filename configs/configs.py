from dotenv import load_dotenv
from os import getenv

try:
    load_dotenv(dotenv_path=".env.development")
    dbname = getenv("dbname","default")
    user = getenv("user","default")
    password = getenv("password","default")
    host = getenv("host","default")
except Exception as err:
    print("env error: ",err)
class Config():
    DEBUG = True
    DATABASE = {
        "dbname":dbname,
        "user":user,
        "password":password,
        "host":host
    }
