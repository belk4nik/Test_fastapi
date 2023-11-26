from typing import List

from fastapi import FastAPI

from pydantic import BaseModel, Field

app = FastAPI(
    title="Audit_PC"
)


data = [
    {"ID": 1001, "Name": "Alexander Ivanov", "Role": "Student"},
    {"ID": 1002, "Name": "Ekaterina Petrova", "Role": "Teacher"},
    {"ID": 1003, "Name": "Maxim Smirnov", "Role": "Administrator"},
    {"ID": 1004, "Name": "Olga Kozlova", "Role": "Student"},
    {"ID": 1005, "Name": "Dmitry Nikolaev", "Role": "Teacher"},
    {"ID": 1006, "Name": "Anna Fedorova", "Role": "Administrator"},
    {"ID": 1007, "Name": "Igor Sokolov", "Role": "Teacher"},
    {"ID": 1008, "Name": "Tatiana Morozova", "Role": "Student"},
    {"ID": 1009, "Name": "Sergey Kuznetsov", "Role": "Administrator"},
    {"ID": 1010, "Name": "Lyudmila Zaytseva", "Role": "Student"}
]

class User(BaseModel):
    ID: int
    Role: str
    Name: str


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in data if user.get("ID") == user_id]


test_OC = [
    {"ID": 1001, "OS": "Windows 10 Pro", "Processor": "Intel Core i5", "RAM": "8GB", "GraphicsCard": "NVIDIA GeForce GTX 1050"},
    {"ID": 1002, "OS": "Linux Ubuntu", "Processor": "AMD Ryzen 7", "RAM": "16GB", "GraphicsCard": "AMD Radeon RX 580"},
    {"ID": 1003, "OS": "Windows 7 Home", "Processor": "Intel Core i7", "RAM": "16GB", "GraphicsCard": "NVIDIA GeForce RTX 2060"},
    {"ID": 1004, "OS": "MacOS", "Processor": "Apple M1", "RAM": "8GB", "GraphicsCard": "Integrated GPU"},
    {"ID": 1005, "OS": "Windows 10 Pro", "Processor": "AMD Ryzen 5", "RAM": "12GB", "GraphicsCard": "NVIDIA GeForce GTX 1660"},
    {"ID": 1006, "OS": "Linux Debian", "Processor": "Intel Core i9", "RAM": "32GB", "GraphicsCard": "AMD Radeon RX 6800 XT"},
    {"ID": 1007, "OS": "Windows 10 Pro", "Processor": "Intel Core i3", "RAM": "4GB", "GraphicsCard": "Integrated GPU"},
    {"ID": 1008, "OS": "MacOS", "Processor": "Apple M1", "RAM": "16GB", "GraphicsCard": "Integrated GPU"},
    {"ID": 1009, "OS": "Linux Ubuntu", "Processor": "AMD Ryzen 3", "RAM": "8GB", "GraphicsCard": "NVIDIA GeForce GTX 1650"},
    {"ID": 1010, "OS": "Windows 10 Pro", "Processor": "Intel Core i5", "RAM": "12GB", "GraphicsCard": "NVIDIA GeForce RTX 3050"}
]

@app.get("/report")
def get_report(limit: int = 5, offset: int = 0):
    return  test_OC[offset:][:limit]

data2 = [
    {"ID": 1001, "Name": "Alexander Ivanov", "Role": "Student"},
    {"ID": 1002, "Name": "Ekaterina Petrova", "Role": "Teacher"},
    {"ID": 1003, "Name": "Maxim Smirnov", "Role": "Administrator"},
    {"ID": 1004, "Name": "Olga Kozlova", "Role": "Student"},
    {"ID": 1005, "Name": "Dmitry Nikolaev", "Role": "Teacher"},
    {"ID": 1006, "Name": "Anna Fedorova", "Role": "Administrator"},
    {"ID": 1007, "Name": "Igor Sokolov", "Role": "Teacher"},
    {"ID": 1008, "Name": "Tatiana Morozova", "Role": "Student"},
    {"ID": 1009, "Name": "Sergey Kuznetsov", "Role": "Administrator"},
    {"ID": 1010, "Name": "Lyudmila Zaytseva", "Role": "Student"}
]


@app.post("/user/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("ID") == user_id, data2))[0]
    current_user["Name"] = new_name
    return {"status": 200, "data": current_user}


class Report(BaseModel):
    ID: int
    user_id : int
    os_name : str
    processors : str
    graphicscard : str


@app.post("/reports")
def add_reports(reports: list[Report]):
    test_OC.extend(reports)
    return {"status": 200, "data": test_OC}