""" User Service """
import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.util.response import Response, ErrorResponse
from app.main.util.messages import USER_MSG


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        # response_object = {
        #     'status': 'success',
        #     'message': 'Successfully registered.'
        # }
        return Response(
            status='Success',
            message=USER_MSG['USER_SAVED']
        ).__dict__, 201
    else:
        return ErrorResponse(), 409


def get_all_users():
    return Response(
        status='Success',
        data=User.query.all(),
        message=USER_MSG['USER_FETCH']
    ).__dict__, 200


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
