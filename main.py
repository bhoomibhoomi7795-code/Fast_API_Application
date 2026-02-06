from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class student(BaseModel):
    name: str
    email: str
    age: int
    Roll_number:str
    Department:str
    
class studentRESPONSE(BaseModel):
    id:int
    name: str
    email: str
    age: int
    Roll_number:str
    Department:str

@app.get("/")
def read_root():
    return {"Hello": "World"}


def create_student(student:student):
    return student
def read_student(student:student):
    return studentResponse(id=id, **student.dict())

def update_student(id:int, student:student):
    return studentResponse(id=id, **student.dict())

def delete_student(id:int):
    return studentResponse(id=id, **student.dict())

@app.post("/student")
def create_student(student:student):
    return create_student(student)

@app.get("/student")
def read_student(student:student):
    return read_student(student)

@app.put("/student/{id}")
def update_student(id:int, student:student):
    return update_student(id, student)

@app.delete("/student/{id}")
def delete_student(id:int):
    return delete_student(id)
