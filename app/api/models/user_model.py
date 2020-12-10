import requests as r
import json
from datetime import datetime as dt
from mongoengine import Document, fields
from mongoengine.errors import DoesNotExist, MultipleObjectsReturned
from app import logger



class UserModel(Document):
    """Parameters model
    """
    _id = fields.ObjectIdField()
    first_name = fields.StringField()
    last_name = fields.StringField()
    contact =fields.StringField()
    dob = fields.DateTimeField(default=None,null=True)
    address = fields.StringField()
    created_at = fields.DateTimeField(default=dt.utcnow)
    updated_at = fields.DateTimeField(default=dt.utcnow)

    meta = {
        "collection": "user"
    }

    def get_all(self,params):
        """
        Get all user from the mongo db database
        :return:
        """
        try:
            user_object = self.__class__.objects()

            response = {
                'code': r.codes.OK,
                'data': json.loads(user_object.to_json())
            }
            return response

        except Exception as e:
            logger.debug(
                f'''
                Exception in parameters_model.get_all
                Error: {e}
                '''
            )
            response = {
                'code': r.codes.INTERNAL_SERVER_ERROR,
                'data': {
                    'message': 'Internal Server Error'
                }
            }
            return response

    def get_one(self,user_oid):
        """
        Get all user from the mongo db database
        :return:
        """
        try:
            user_object = self.__class__.objects.get(
                _id=user_oid
            )

            response = {
                'code': r.codes.OK,
                'data': json.loads(user_object.to_json())
            }
            return response

        except DoesNotExist:
            response = {
                'code': r.codes.NOT_FOUND,
                'data': {
                    'message': f'User Notfound with {"uses_oid"}'
                }
            }
            return response

        except Exception as e:
            logger.debug(
                f'''
                Exception in parameters_model.get_one
                Error: {e}
                '''
            )
            response = {
                'code': r.codes.INTERNAL_SERVER_ERROR,
                'data': {
                    'message': 'Internal Server Error'
                }
            }
            return response

    def add_one(self, params):
        """
        add one user in mongodb database
        Parameter:
        ----------------------
        :param first_name: str
        :param contact: str
        :param last_name: str
        :param dob_name: str
        :param address_name: str
        """
        try:


            if int(len(params['contact'])) != 10 :
                response = {
                    'code': r.codes.BAD_REQUEST,
                    'data': {
                        'message': f'Please enter valid contact number {params["contact"]}'
                    }
                }
                return response


            user_object = self.__class__.objects.get(
                contact=params['contact']
            )
            response =  {
                'code': r.codes.CONFLICT,
                'data': {
                    'message': f'user already exist with contact number {params["contact"]}'
                }
            }
            return response

        except DoesNotExist:

            try:
                user_object = self.__class__(
                    first_name=params['first_name'],
                    last_name=params['last_name'],
                    contact=str(params['contact']),
                    dob=params['dob'],
                    address=params['address'],
                    created_at=dt.utcnow(),
                    updated_at=dt.utcnow()
                )

                user_object.save()

                response = {
                    'code': r.codes.CREATED,
                    'data': {
                        'message': 'User Created'
                    }
                }
                return  response
            except Exception as e:
                logger.debug(
                    f'''
                    Exception in user_model.add_one()
                    Error: {e}
                    '''
                )
                response = {
                    'code': r.codes.INTERNAL_SERVER_ERROR,
                    'data': {
                        'message': 'Internal Server Error'
                    }
                }
                return response

        except MultipleObjectsReturned:
            response = {
                'code': r.codes.INTERNAL_SERVER_ERROR,
                'data': {
                    'message': f'Multiple user found with {params["contact"]}'
                }
            }
            return response
        except Exception as e:
            logger.debug(
                f'''
                Exception in user_model.add_one()
                Error: {e}
                '''
            )
            response = {
                'code': r.codes.INTERNAL_SERVER_ERROR,
                'data': {
                    'message': 'Internal Server Error'
                }
            }
            return response

    def update_one(self,params):
        """
        Update user information by user id
         Parameter:
        ----------------------
        :param first_name: str
        :param contact: str
        :param last_name: str
        :param dob_name: str
        :param address_name: str
        :return:
        """
        try:
            user_object = self.__class__.objects.get(
                _id=params['user_oid']
            )
            if 'first_name' in params and params['first_name']:
                user_object.first_name = params['first_name']
            if 'last_name' in params and params['last_name']:
                user_object.last_name = params['last_name']
            if 'dob' in params and params['dob']:
                user_object.dob = params['dob']
            if 'address' in params and params['address']:
                user_object.address = params['address']

            user_object.updated_at = dt.utcnow()
            user_object.save()
            response = {
                'code': r.codes.OK,
                'data': {
                    'message': 'User Updated!'
                }
            }
            return response

        except DoesNotExist:
            response = {
                'code': r.codes.NOT_FOUND,
                'data': {
                    'message': f'User Notfound with {params["uses_oid"]}'
                }
            }
            return response

        except MultipleObjectsReturned:
            response = {
                'code': r.codes.INTERNAL_SERVER_ERROR,
                'data': {
                    'message': f'Multiple user found with {params["contact"]}'
                }
            }
            return response

        except Exception as e:
            logger.debug(
                f'''
                Exception in user_model.update_one()
                Error: {e}
                '''
            )
            response = {
                'code': r.codes.INTERNAL_SERVER_ERROR,
                'data': {
                    'message': 'Internal Server Error'
                }
            }
            return response

    def delete_one(self,user_oid):
        """
        DELETE user by user _id
        :return:
        """
        try:
            user_object = self.__class__.objects.filter(_id=user_oid)
            user_object.delete()
            response = {
                'code': r.codes.OK,
                'data': {
                    'message': 'User Deleted!'
                }
            }
            return response

        except DoesNotExist:
            response = {
                'code': r.codes.NOT_FOUND,
                'data': {
                    'message': f'User Notfound with {user_oid}'
                }
            }
            return response
        except MultipleObjectsReturned:
            response = {
                'code': r.codes.INTERNAL_SERVER_ERROR,
                'data': {
                    'message': f'Multiple user found with {"user_id"}'
                }
            }
            return response
        except Exception as e:
            logger.debug(
                f'''
                Exception in user_model.delete_one()
                Error: {e}
                '''
            )
            response = {
                'code': r.codes.INTERNAL_SERVER_ERROR,
                'data': {
                    'message': 'Internal Server Error'
                }
            }
            return response
