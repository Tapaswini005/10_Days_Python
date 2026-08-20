def analyze_number(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

number = int(input("Enter a number: "))
analyze_number(number)