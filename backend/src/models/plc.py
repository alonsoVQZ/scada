
from . import db

class PLC(db.Model):
    __tablename__ = 'plcs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    model = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    tags = db.relationship('Tag', backref='plc', lazy=True)

    def __repr__(self):
        return f'<PLC {self.name}>'
