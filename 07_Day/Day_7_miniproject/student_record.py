name = input("Enter student name: ")
age = input("Enter student age: ")

with open("students.txt", "a") as file:
    file.write(f"Name: {name}, Age: {age}\n")

print("Student record saved successfully!")