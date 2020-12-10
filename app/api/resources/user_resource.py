from flask_restful import Resource, reqparse
from app.libs.response_utils import ResponseUtil
from app.api.models.user_model import UserModel
from bson.json_util import ObjectId
import requests as r


class UserResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self,**kwargs):
        """Get all users
        """
        self.parser.add_argument(
            'limit', required=False, type=int, location='args'
        )
        self.parser.add_argument(
            'page', required=False, type=int, location='args'
        )
        self.parser.add_argument(
            'querystring', required=False, type=str, location='args'
        )
        self.args = self.parser.parse_args()

        response = UserModel().get_all(self.args)

        return ResponseUtil(response['code']).json_response(response['data'])

    def post(self,**kwargs):
        """Get all users
        """
        self.parser.add_argument(
            'first_name', required=True, type=str, location='json'
        )
        self.parser.add_argument(
            'last_name', required=True, type=str, location='json'
        )
        self.parser.add_argument(
            'dob', required=False, type=str, location='json'
        )
        self.parser.add_argument(
            'contact', required=False, type=str, location='json'
        )
        self.parser.add_argument(
            'address', required=False, type=str, location='json'
        )
        self.args = self.parser.parse_args()

        response = UserModel().add_one(self.args)

        return ResponseUtil(response['code']).json_response(response['data'])

class UserSingleResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self, user_id):
        """Get all users
        """
        if not ObjectId.is_valid(user_id):
            response = {
                'code': r.codes.BAD_REQUEST,
                'data': {
                    'message': f'user is not valid object ID {user_id}'
                }
            }
            return ResponseUtil(response['code']).json_response(response['data'])
        else:

            response = UserModel().get_one(user_id)

        return ResponseUtil(response['code']).json_response(response['data'])

    def put(self,user_id):
        """Get all users
        """
        if not ObjectId.is_valid(user_id):
            response = {
                'code': r.codes.BAD_REQUEST,
                'data': {
                    'message': f'user is not valid object ID {user_id}'
                }
            }
            return ResponseUtil(response['code']).json_response(response['data'])

        self.parser.add_argument(
            'first_name', required=True, type=str, location='json'
        )
        self.parser.add_argument(
            'last_name', required=True, type=str, location='json'
        )
        self.parser.add_argument(
            'dob', required=False, type=str, location='json'
        )
        self.parser.add_argument(
            'contact', required=False, type=str, location='json'
        )
        self.parser.add_argument(
            'address', required=False, type=str, location='json'
        )
        self.args = self.parser.parse_args()

        self.args['user_oid'] = ObjectId(user_id)

        response = UserModel().update_one(self.args)

        return ResponseUtil(response['code']).json_response(response['data'])

    def delete(self,user_id):
        """
        Delete user by user id
        :param user_id:
        :return:
        """
        if not ObjectId.is_valid(user_id):
            response = {
                'code': r.codes.BAD_REQUEST,
                'data': {
                    'message': f'user is not valid object ID {user_id}'
                }
            }
            return ResponseUtil(response['code']).json_response(response['data'])

        response = UserModel().delete_one(ObjectId(user_id))

        return ResponseUtil(response['code']).json_response(response['data'])

