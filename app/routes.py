from flask import Flask,render_template,request,jsonify
from app.services import get_students,delete_student_by_id,edit_student
from app.models import db,Student
from random import randint
import json
# function register routes
def register_routes(app:Flask):
    try:
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
                    id = randint(20,2000)
                    age =  request.form['age']
                    Student.add_student(id=id,name=name,age=age)
                    students = get_students()
                    return render_template("form.html",data=students)
                else:
                    students = get_students()
                    return render_template("form.html",data=students)
            except Exception as err:
                print("error studentRoute(): ",err)
                return "error studentRoute():"
        # 
        @app.route("/students")
        def get_all_students():
            try:
                
                # query
                page = request.args.get('page',1,type=int)
                limit = request.args.get('limit',2,type=int)
                search = request.args.get('search','',type=str)
                sort = request.args.get('sort','{}')
                filter_str = request.args.get('filter','{}')
                query = Student.query
                per_page = limit
                try:
                    filter_dict = json.loads(filter_str)
                except json.JSONDecoder as err:
                    filter_dict = {}
                    print("json error: ",err)
                # print(filter_dict)
                # for key,value in filter_dict.items():
                #     attr = getattr(Student, key)
                #     if isinstance(value, dict):
                #         if 'min' in value and 'max' in value:
                #             # filter_condition = (attr>=value['min'] & attr <=value['max'])
                #             print(value['min'],value['max'])
                #         elif 'min' in value:
                #             print()
                #             # filter_condition = (attr >= value['min'])
                #         elif 'max' in value:
                #             print()
                #             # filter_condition = (attr <= value['max'])
                #         # print("filter_condition: ",filter_condition)
                #     else:
                #         filter_condition = (attr == value)
                        # print("filter_condition: ",filter_condition)
                # print("filter_condition: ",filter_condition)
                data = get_students()
                return jsonify(data)
            except Exception as err:
                print("Error: ",err)
        # 
        @app.route("/student/<int:id>",methods=['DELETE','PUT','GET'])
        def ImmuteStudentById(id):
            try:
                if(request.method=='DELETE'):
                    
                    Student.delete_student(id)
                    # db.session.delete(user_to_delete)
                    # db.session.commit()
                    return jsonify({"message": "Student deleted"})
                elif(request.method=='PUT'):
                    # name =  request.form['name'] # as form data
                    # age = request.form['age']
                    # data = edit_student(id,name) #custome
                    user_to_edit = Student.query.get_or_404(id)
                    data = request.get_json() # as json data
                    Student.edit_student(id=id,new_data=data)
                    return data
                elif request.method == 'GET':
                    data = Student.get_student_by_id(id)
                    return jsonify(data)
            except Exception as err:
                print("Error ImmuteStudentById(): ",err)
                return
        @app.route("/db")
        def getDBTest():
            user1 = Student(id=256,name="this is me")
            try:
                anyth = db.session.add(user1)
                db.session.commit()
                return "Hello"
            except Exception as err:
                print("error to add: ",err)
    except Exception as err:
        print("register route err: ",err)