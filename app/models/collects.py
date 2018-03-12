from app.extensions import db

class Collects(db.Model):
    __tablename__ = 'collects'
    id = db.Column(db.Integer, primary_key=True)
    img_id = db.Column(db.String(64))
    topics_id = db.Column(db.String(32))
    pid = db.Column(db.Integer)