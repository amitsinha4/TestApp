""" Data Transfer object """
from flask_restplus import Namespace, fields


class UserDto:
    """ UserDto """
    api = Namespace('user', description='user related operations')

    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        # 'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier'),
        'registered_on': fields.String
    })

    user_data = api.model('user_data', {
        'message': fields.String,
        'status': fields.String,
        'data': fields.Nested(user)
    })


class PageDto:
    """ PageDto """
    api = Namespace('page', description='Page related operations')
    page = api.model('Page', {
        'page_name': fields.String(required=True, description='Page Name'),
        'page_id': fields.String(required=True, description='Page ID'),
        'is_active': fields.Boolean(required=True, description='Page Status')
    })

    page_of_pages = api.model('Page of Pages', {
        'status': fields.String(required=True),
        'data': fields.Nested(page),
        'message': fields.String(required=False)
    })
