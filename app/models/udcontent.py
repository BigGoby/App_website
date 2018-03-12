from app.extensions import db

class Udcontent(db.Model):
    __tablename__ = 'udcontent'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(32))
    ud_id = db.Column(db.Integer)
    pid = db.Column(db.Integer)