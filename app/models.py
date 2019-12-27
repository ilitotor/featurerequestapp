from app import db
from datetime import datetime


class Feature(db.Model):
    id_feature = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    client = db.Column(db.String(80), nullable=False)
    client_priority = db.Column(db.Integer, nullable=False)
    target_date = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, nullable=False
    )
    product_area = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return "Title: {}".format(self.title)