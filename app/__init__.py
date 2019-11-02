""" Api UOM """
from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.page_controller import api as page_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='MyTest Appication',
          version='1.2.5',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(page_ns, path='/page')
