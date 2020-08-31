class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here

    def id(self):
        print(self.name[0] + self.last_name + self.birth_year)


name_of_student = input()
last_name_student = input()
date_of_birthday = input()

student = Student(name_of_student, last_name_student, date_of_birthday)
student.id()
