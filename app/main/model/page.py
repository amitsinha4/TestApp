""" Pages Model """
from .. import db

class AboutPage(db.Model):
    """ AboutPage """
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    page_name = db.Column(db.String(100), nullable=True)
    page_id = db.Column(db.String(10), nullable=False)
    is_active = db.Column(db.Integer(), nullable=True)

    def __repr__(self):
        """Repr Function"""
        return "<AboutPage {}".format(self.page_name)
