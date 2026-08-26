class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)

name = input("Enter Name: ")
age = int(input("Enter Age: "))
branch = input("Enter Branch: ")

student = Student(name, age, branch)
student.display()