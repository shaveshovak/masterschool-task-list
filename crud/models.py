from db import db

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<ToDo {self.task}>'
