class Person:
    def display(self):
        print("I am a Person")

class Student(Person):
    pass

student = Student()
student.display()