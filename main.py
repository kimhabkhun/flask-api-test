from app import create_app
from configs.configs import Config

try:
    app = create_app(Config.Db_Config)
except Exception as err:
    print("main errr: ",err)

if __name__ == "__main__":
    app.run(debug=True)