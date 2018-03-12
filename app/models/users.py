from app.extensions import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer)
    phone_num = db.Column(db.Integer)
    password = db.Column(db.String(128))

