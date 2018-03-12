from app.extensions import db

class Topics(db.Model):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    top_img = db.Column(db.String(64))
    top_title = db.Column(db.String(32))
    top_content = db.Column(db.Text)
    house_type = db.Column(db.String(32))
    usable_area = db.Column(db.Integer)
    ratchadapisek = db.Column(db.String(32))
    decorate_cost = db.Column(db.Integer)
    count = db.Column(db.Integer)
    pid = db.Column(db.Integer)
    comment = db.Column(db.String(32))
    floor_plan = db.Column(db.String(32))
    house_type_content = db.Column(db.String(32))