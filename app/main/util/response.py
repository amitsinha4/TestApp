""" Response Module """
import sys
import traceback


# Response Class
class Response:
    """ Response Class """

    def __init__(self, status=None, data=None, message=None):
        self.status = status
        self.data = data
        self.message = message


# Error Response
class ErrorResponse:
    """ Error Response """

    def __init__(self, message=''):
        if not message:
            message = 'System Error'
        self.is_success = False
        self.response = []
        self.error_message = message
        self.error_info = ''

    @staticmethod
    def get_error_message():
        """ Getting Error Message """
        exc_type, exc_value, exc_traceback = sys.exc_info()
        value = repr(traceback.format_exception(
            exc_type, exc_value, exc_traceback))
        return value
