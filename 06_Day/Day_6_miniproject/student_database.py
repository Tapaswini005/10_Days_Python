student = {
    "name": input("Enter Name: "),
    "age": int(input("Enter Age: ")),
    "branch": input("Enter Branch: ")
}

print("\n===== STUDENT DATABASE =====")
for key, value in student.items():
    print(key, ":", value)