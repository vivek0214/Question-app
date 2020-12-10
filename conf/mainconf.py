import pymongo
import os
from flask import Config


""" Common config can go here"""

STATIC_FOLDER = os.path.dirname(os.path.abspath(
    __file__)).replace("conf", "app/static")


class DevelopmentConfig(Config):
    # MongoDB Database configuration

    MONGODB_DATABASE = 'rest_db'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = 'rest_db'
    MONGODB_PASSWORD = 'rest_pass123'

    STATIC_FOLDER = STATIC_FOLDER


class ProductionConfig(Config):
    # MongoDB Database configuration
    MONGODB_DATABASE = 'rest_db'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = 'rest_db'
    MONGODB_PASSWORD = 'rest_pass123'
