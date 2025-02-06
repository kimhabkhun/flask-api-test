from configs.db import get_connection
from random import randint
from app.utils import formator
def get_students():
    
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM student;")
    data = cur.fetchall()
    data = formator(data,["id","name"])
    # def dic_format():
    #     listedData = []
    #     for i in range(len(data)):
    #         new_data = {}
    #         new_data['id'] = data[i][0]
    #         new_data['name'] = data[i][1]
    #         # print(new_data)
    #         listedData.append(new_data)
    #     return listedData
    # # print("new data: ",dic_format())
    # data = dic_format()
    conn.close()
    return data

def add_student(id:int,value):
    conn = get_connection()
    random_id = randint(1,2000)
    # print("random id: ",random_id)
    cur = conn.cursor()
    cur.execute("INSERT INTO student (id, name) VALUES (%s, %s);",(random_id,value))
    conn.commit()
    conn.close()
def edit_student(id:int,value:str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"UPDATE student SET name=%s WHERE id=%s;",(value,id))
    conn.commit()
    cur.execute(f"SELECT * FROM student WHERE id={id};")
    data = cur.fetchall()
    def dic_format():
        listedData = []
        for i in range(len(data)):
            new_data = {}
            new_data['id'] = data[i][0]
            new_data['name'] = data[i][1]
            # print(new_data)
            listedData.append(new_data)
        return listedData
    # print("new data: ",dic_format())
    data = dic_format()
    conn.close()
    return data

def delete_student_by_id(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM student WHERE id = {id}")
    conn.commit()
    conn.close()