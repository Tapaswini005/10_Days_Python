students = []

def add_student():
    try:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        branch = input("Enter Branch: ")

        student = {
            "name": name,
            "age": age,
            "branch": branch
        }

        students.append(student)

        with open("students.txt", "a") as file:
            file.write(f"{name},{age},{branch}\n")

        print("Student Added Successfully!")

    except ValueError:
        print("Please enter a valid age!")

def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("No student records found.")
            else:
                print("\n===== STUDENT RECORDS =====")
                for record in data:
                    print(record.strip())

    except FileNotFoundError:
        print("No records found!")

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")