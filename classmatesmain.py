from threading import local

from pyscript import display, document

class student:
    def __init__(self, name, section, favoritesubject):
        self.name = name
        self.section = section
        self.favoritesubject = favoritesubject

student = [
    student("Allie", "Emerald", "Values Education"),
    student("Kyla", "Emerald", "Math"),
    student("James", "Emerald", "SS"),
    student("Sofia", "Emerald", "ICT"),
]

def add(e):
    document.getElementById('output').innerHTML = ""

    name = document.getElementById('name').value
    section = document.getElementById('section').value
    favoritesubject = document.getElementById('favoritesubject').value

    global student67 # SIX SEVENNN
    student67 = student(name, section, favoritesubject)

    display(f'{student67.name} is in {student67.section}. Their favorite subject is {student67.favoritesubject}.', target='output')

def introduce(e):
    document.getElementById('output').innerHTML = ""

    global student1, student2, student3, student4, student5, student6

    display(f'Hi I am {student1.name}! I am from {student1.section}. My favorite subject is {student1.subject}.', target='output')
    display(f'Hi I am {student2.name}! I am from {student2.section}. My favorite subject is {student2.subject}.', target='output')
    display(f'Hi I am {student3.name}! I am from{student3.section}. My favorite subject is {student3.subject}.', target='output')
    display(f'Hi I am {student4.name}! I am from{student4.section}. My favorite subject is {student4.subject}.', target='output')
    display(f'Hi I am {student5.name}! I am from{student5.section}. My favorite subject is {student5.subject}.', target='output')
    display(f'Hi I am {student67.name}! I am from{student67.section}. My favorite subject is {student67.subject}.', target='output')



    student1 = student1
    student2 = student2
    student3 = student3
    student4 = student4
    student5 = student5
    student67 = student67

def show_list(event):
    list_div = document.getElementByid("list")

    if list_div.innerHTML != "":
       list_div.innerHTML = ""

    else:
        for mates in student:
            display(student.introduce(), target="list")



              
