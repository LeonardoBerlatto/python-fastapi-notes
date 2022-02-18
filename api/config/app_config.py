import os
import urllib.parse

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = 'development'
    DEBUG: bool = True
    APP_HOST: str = '0.0.0.0'
    APP_PORT: int = 8000
    MONGO_URL: str
    DATABASE: str = 'notes'


class LocalConfig(Config):
    MONGO_URL: str = f'mongodb://{urllib.parse.quote_plus("root")}:{urllib.parse.quote_plus("root")}@localhost:27017'


class ProductionConfig(Config):
    MONGO_URL: str = os.getenv('MONGO_URL', '')
    DEBUG: str = False


def get_config():
    env = os.getenv('ENV', 'local')
    config_type = {
        'local': LocalConfig(),
        'production': ProductionConfig(),
    }
    return config_type[env]


config = get_config()
