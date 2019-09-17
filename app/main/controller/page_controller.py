""" Page Controller """
from flask import request
from flask_restplus import Resource

from ..util.dto import PageDto
from app.main.service.page_service import get_page, save_page

api = PageDto.api
_page = PageDto.page_of_pages


@api.route('/')
class AboutPageAPI(Resource):
    """ About Page Api's """
    @api.doc('List of pages')
    @api.marshal_with(_page)
    def get(self):
        return get_page()

    @api.expect(_page)
    @api.doc('Save a Page')
    def post(self):
        data = request.json
        return save_page(data)
