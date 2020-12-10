import os
from flask import Flask

import pymongo, json
from flask_cors import CORS
from mongoengine import connect



app = Flask(__name__, static_url_path='/static')
#app = Flask(__name__)
CORS(app, support_credentials=True)

environment = os.environ.get('hps_env', 'development')

if environment == 'production':
    app.config.from_object('conf.mainconf.ProductionConfig')
else:
    app.config.from_object('conf.mainconf.DevelopmentConfig')

""" Initiating the logger"""
logger = app.logger
logger.setLevel('DEBUG')


#database set up for MongoDB
# try:
#     db = connect(
#         host='mongodb://{}:{}@localhost:27017/{}'.format(
#             app.config.get('MONGODB_USERNAME'),
#             app.config.get('MONGODB_PASSWORD'),
#             app.config.get('MONGODB_DATABASE')
#         )
#     )
#     dbnames = db.database_names()
#     #dbnames = db.hps_activity_db
#
# except pymongo.errors.ServerSelectionTimeoutError as err:
#     print(err)

app.secret_key = '5!RY|Oa4TpL8@d@g^|L1NYtcsKZd^g6b'

# import all dependencies
from app.api.routes.user_route import *

# testing url
@app.route('/')
def statusRoute():
    return json.dumps({"status" : True, "app": "Rest APIs Services"})

















