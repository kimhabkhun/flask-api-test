import psycopg2
from configs.configs import Config

def get_connection():
    try:
        conn = psycopg2.connect(dbname=Config.DATABASE['dbname'],user=Config.DATABASE['user'],password=Config.DATABASE['password'],host=Config.DATABASE['host'])
        print("db connection successfully!✅")
        return conn
    except psycopg2.Error as err:
        print("Database connection error: ",err)
        return None