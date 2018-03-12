from app.extensions import db

class Personal(db.Model):
    __tablename__ = 'personal'
    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(64), default='default.jpg')
    nickname = db.Column(db.String(20), unique=True)
    sex = db.Column(db.Boolean, default=None)
    address = db.Column(db.String(64))
    birthday = db.Column(db.DateTime, default=None)
    introduce = db.Column(db.Text)
    user_id = db.Column(db.Integer)