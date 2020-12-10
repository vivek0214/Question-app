from flask_restful import Api
from app import app
from app.api.resources.user_resource import UserResource ,UserSingleResource
api = Api(app)


api.add_resource(
    UserResource,'/api/v1/user', endpoint='User_Resource'
)

api.add_resource(
    UserSingleResource,'/api/v1/user/<user_id>', endpoint='User_Single_Resource'
)