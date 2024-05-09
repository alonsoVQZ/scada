from . import db

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    plc_id = db.Column(db.Integer, db.ForeignKey('plcs.id'), nullable=False)
    data_type = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(255))

    def __repr__(self):
        return f'<Tag {self.name}>'
