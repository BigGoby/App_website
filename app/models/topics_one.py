from app.extensions import db

class Topics_one(db.Model):
    __tablename__ = 'topics_one'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    content = db.Column(db.String(32))

