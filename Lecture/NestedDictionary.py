student = {
    "name":"Rahul Kuamr",
    "subject":{
        "phy":90,
        "eng":80,
        "math":100
    },
    "company":'PwC'
    
}

print(student)
print(student["subject"]["math"])

print(student.keys())
print(student.values())
print(len(student))

print(list(student["subject"]))

print(student.items())

print(student.get("name"))

new_dict = {"city": "delhi"}

student.update(new_dict)
print(student)
