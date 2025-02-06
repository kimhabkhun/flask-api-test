from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    def __repr__(self):
        return f"({self.id},{self.name})"
    def get_student(self):
        return {
            'id':self.id,
            'name':self.name
        }
    def add_student(self):
        db.session.add(self)
        db.session.commit()
    