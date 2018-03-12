from app.extensions import db

class Styles(db.Model):
    __tablename__ = 'styles'
    id = db.Column(db.Integer, primary_key=True)
    imgUrl = db.Column(db.String(32))
    describe = db.Column(db.String(32))
    type = db.Column(db.String(32))
    pid = db.Column(db.Integer)