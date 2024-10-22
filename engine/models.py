from . import db

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50))

    def __repr__(self) -> str:
        return f"Task set with the id {self.id}"