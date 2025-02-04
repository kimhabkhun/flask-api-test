from flask import Flask,render_template,request,jsonify
from app.services import get_students,add_student,delete_student_by_id
# function register routes
def register_routes(app:Flask):
    # 
    @app.route("/")
    @app.route("/home")
    def getHomePage():
        try:
            return render_template("index.html")
        except Exception as err:
            print("Error getHomePage(): ",err)
    # 
    @app.route("/student",methods=['GET','POST'])
    def studentRoute():
        try:
            if(request.method=='POST'):
                name =  request.form['name']
                id =  request.form['id']
                add_student(int(id),name)
                students = get_students()
                return render_template("form.html",data=students,name=name,id=len(students)+1)
            else:
                students = get_students()
                return render_template("form.html",data=students)
        except Exception as err:
            print("error studentRoute(): ",err)
    # 
    @app.route("/student/<id>",methods=['DELETE'])
    def deleteById(id):
        try:
            if(request.method=='DELETE'):
                delete_student_by_id(int(id))
                return jsonify({"message": "Student deleted"})
        except Exception as err:
            print("Error deleteById(): ",err)
            return