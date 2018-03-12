from datetime import datetime

from app.extensions import db

class Information(db.Model):
    __tablename__ = 'information'
    id = db.Column(db.Integer, primary_key=True)
    imgurl = db.Column(db.String(64), default=None)
    title = db.Column(db.String(64))
    time = db.Column(db.DateTime,default=datetime.utcnow)
    content = db.Column(db.String(64))
