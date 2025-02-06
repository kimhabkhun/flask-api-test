from flask import Flask,render_template,request,jsonify
from app.services import get_students,delete_student_by_id,edit_student
from app.models import db,Student
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
                    id =  request.form['id']
                    # add_student(int(id),name) this is custome function using query
                    user_to_add = Student(id=int(id),name=name)
                    db.session.add(user_to_add)
                    db.session.commit()
                    students = get_students()
                    return render_template("form.html",data=students,name=name,id=len(students)+1)
                else:
                    students = get_students()
                    return render_template("form.html",data=students)
            except Exception as err:
                print("error studentRoute(): ",err)
        # 
        @app.route("/students")
        def get_all_students():
            try:
                
                # query
                # page = request.args.get('page',1,int)
                # limit = request.args.get('limit',2,int)
                # search = request.args.get('search','',str)
                # sort = request.args.get('sort','{}',str)
                # print(page,limit,search,sort)
                # per_page = 10
                
                # query = Student.query
                
                # if len(search)!=0:
                #     query = query.filter(Student.name.ilike(f'%{search}%'))
                # print(query)
                
                # pagination = query.paginate(page=page,per_page=per_page)
                # # print("search student: ",pagination)
                # students = query.all()
                # # students = pagination.items
                # print(students)
                
                # for i in range(len(students)):
                #     myStd = str(students[i])
                #     type(myStd)
                    # myStd = myStd.rsplit(")")
                
                # for i in range(len(students)):
                    # print(f"student {i}: ",type(students[i]),students[i])
                # print("student: ",type(students),len(students))
                data = get_students()
                return jsonify(data)
            except Exception as err:
                print("Error: ",err)
        # 
        # @app.route("/student/<int:id>",methods=['DELETE','PUT']) #set type int for id
        @app.route("/student/<int:id>",methods=['DELETE','PUT','GET'])
        def ImmuteStudentById(id):
            try:
                if(request.method=='DELETE'):
                    # delete_student_by_id(int(id))
                    user_to_delete = Student.query.get_or_404(id)
                    print("user to delete",user_to_delete)
                    db.session.delete(user_to_delete)
                    db.session.commit()
                    return jsonify({"message": "Student deleted"})
                elif(request.method=='PUT'):
                    # name =  request.form['name']
                    # data = edit_student(id,name) #custome
                    user_to_edit = Student.query.get_or_404(id)
                    data = request.get_json()
                    if 'name' in data:
                        user_to_edit.name = data['name']
                    db.session.commit()
                    return data
                elif request.method == 'GET':
                    user_to_get = Student.query.get(id)
                    # print("type of user: ",type(user_to_get))
                    # print("this is user: ",user_to_get.id)
                    print(Student.to_dict)
                    data = {
                        "id":user_to_get.id,
                        "name":user_to_get.name,
                    }
                    print(data)
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