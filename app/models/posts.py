from datetime import datetime

from app.extensions import db

class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, index=True, default=0)
    content = db.Column(db.Text)
    title = db.Column(db.String(32))
    counts = db.Column(db.Integer, default=0)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    pimg = db.Column(db.String(32))
    type = db.Column(db.String(32))
    pid = db.Column(db.Integer)
    p_id = db.Column(db.Integer)