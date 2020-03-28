""" Manage File """
import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import jsonify
from app.main import create_app, db
from app.main.model import user
from app.main.model import page
from werkzeug.exceptions import HTTPException
# Importing Blue Print
from app import blueprint

app = create_app(os.getenv('ENV') or 'dev')

app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@app.errorhandler(Exception)
def handle_error(e):
    """ Hanlde Error """
    code = 500
    print("----------------------")
    if isinstance(e, HTTPException):
        code = e.code
        print(e)
        return jsonify(str(e)), code

@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
