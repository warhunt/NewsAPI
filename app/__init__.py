import logging
from logging.config import dictConfig

from flask_cors import CORS
import connexion

from app.database import db
from app.config import ConfigFactory

import app.news.controllers as news

def create_app():
    try:
        app_connexion = connexion.FlaskApp(__name__, specification_dir='openapi/')
        app_connexion.add_api('openapi.yaml')
        application = app_connexion.app

        application.config.from_object(ConfigFactory.factory())

        CORS(application, resources={r"/*": {"origins": "*"}})

        dictConfig(application.config.get('LOGGING'))
        application.logger = logging.getLogger(application.config['LOGGER_NAME'])
        db.init_app(application)
            
        application.register_blueprint(news.module)
    except Exception as exp:
        application.logger.critical(str(exp))
    finally:
        application.logger.info("---API is created---")
        return app_connexion