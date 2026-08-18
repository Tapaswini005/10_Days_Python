name = input("Enter Name: ")
marks = int(input("Enter Marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print("\nResult")
print("Name:", name)
print("Grade:", grade)