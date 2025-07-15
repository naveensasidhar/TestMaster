# contact list as dictionary.
contacts ={
    "number": 4,
    "students":[
        {"name": "Naveen Sasidharan", "email": "naveencem@gmail.com"},
         {"name": "Bipsa Purushothaman", "email": "bisppu@gmail.com"},
         {"name": "Neha Anil", "email": "nehaanil@gmail.com"},
         {"name": "Nihal Anil", "email": "nihalanil@gmail.com"}
    ]
}

# print out only the email to create email group
print("Student emails")
for student in contacts["students"]:
    print(student)
    print(student["email"])