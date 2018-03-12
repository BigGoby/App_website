from app.extensions import db

class Diary(db.Model):
    __tablename__ = 'diary'
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String(32))
    imgurl = db.Column(db.String(64), default=None)
    house_money = db.Column(db.String(32))
    usable_area = db.Column(db.String(32))
    house_type = db.Column(db.String(32))
    house_style = db.Column(db.String(32))
    content = db.Column(db.String(64))
    pid = db.Column(db.Integer)