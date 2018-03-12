from app.extensions import db

class Design(db.Model):
    __tablename__ = 'design'
    id = db.Column(db.Integer, primary_key=True)
    logo = db.Column(db.String(64))
    title = db.Column(db.String(32))
    content = db.Column(db.Text)
    company = db.Column(db.String(32))
    address = db.Column(db.String(32))
    pid = db.Column(db.Integer)