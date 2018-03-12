from app.extensions import db

class UnderDiscussion(db.Model):
    __tablename__ = 'underdiscussion'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    content = db.Column(db.String(32))
    imgurl = db.Column(db.String(32))