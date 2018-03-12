from app.extensions import db

class Topics_udcontent(db.Model):
    __tablename__ = 'topics_udcontent'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(32))
    imgurl1 = db.Column(db.String(32))
    imgurl2 = db.Column(db.String(32))
    imgurl3 = db.Column(db.String(32))
    topics_one_id = db.Column(db.Integer)
    pid = db.Column(db.Integer)