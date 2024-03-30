# from fastapi import FastAPI
# import unvicorn 

# app  = FastAPI()

# @app.get("/")
# def todos():
#     print("Hello world")
#     return "Hello return"

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    grade: str

class StudentDB:
    def __init__(self):
        self.students = {}
        self.next_id = 1

    def get_all_students(self):
        return self.students

    def get_student_by_id(self, student_id: int):
        return self.students.get(student_id)

    def add_student(self, student: Student):
        self.students[self.next_id] = student
        self.next_id += 1
        return self.next_id - 1

    def update_student(self, student_id: int, student: Student):
        if student_id not in self.students:
            raise HTTPException(status_code=404, detail="Student not found")
        self.students[student_id] = student

    def delete_student(self, student_id: int):
        if student_id not in self.students:
            raise HTTPException(status_code=404, detail="Student not found")
        del self.students[student_id]


db = StudentDB()

@app.get("/students")
def get_all_students():
    return db.get_all_students()

@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = db.get_student_by_id(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/students")
def create_student(student: Student):
    student_id = db.add_student(student)
    return {"student_id": student_id}

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    db.update_student(student_id, student)
    return {"message": "Student updated successfully"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    db.delete_student(student_id)
    return {"message": "Student deleted successfully"}

def start ():
    unvicorn.run("todosapp.main:app" , host ="127.0.0.1" , port = 8080)

















# from typing import Union
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     print("hello todos ")
#     return "Hello world"
    