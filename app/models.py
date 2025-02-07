from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    # def __repr__(self):
    #     return f"({self.id},{self.name},{self.age})"
    def get_student(self):
        return {
            'id':self.id,
            'name':self.name,
            'age':self.age,
        }
        
    def get_student_by_id(id):
        user_to_find = Student.query.get(id)
        return {
            'id':user_to_find.id,
            'name':user_to_find.name,
            'age':user_to_find.age,
        }
        
    def add_student(id,name,age):
        user_to_add = Student(id=int(id),name=name,age=int(age))
        db.session.add(user_to_add)
        db.session.commit()
        
    def delete_student(id):
        user_to_delete = Student.query.get_or_404(id)
        db.session.delete(user_to_delete)
        db.session.commit()
    
    def edit_student(id,new_data):
        user_to_edit = Student.query.get_or_404(id)
        if 'name' in new_data:
            user_to_edit.name = new_data['name']
        if 'age' in new_data:
            user_to_edit.age = new_data['age']
        db.session.commit()
