from pymongo import MongoClient

from api.config import config

mongo_client = MongoClient(config.MONGO_URL)

database = mongo_client[config.DATABASE]
