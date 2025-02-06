from flask import Flask
from configs.configs import Config
from app.blog import blog
from flask_migrate import Migrate
from app.routes import register_routes
from app.models import db
migrate = Migrate()

def create_app(config_class=Config.Db_Config):
    try:
        app = Flask(__name__,template_folder='../templates',instance_relative_config=True)
        #
        app.config.from_object(config_class)
        db.init_app(app) # for flask_sqlalchemy they no init when created so we need to init
        migrate.init_app(app,db)
        # register routes
        app.register_blueprint(blog,url_prefix='/blog')
        
        register_routes(app)
        return app
    except Exception as err:
        print("create app error: ",err)
        return None