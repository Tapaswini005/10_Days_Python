# Day 4 - Loops and Functions

## Introduction

Loops are used to execute a block of code repeatedly. Functions are reusable blocks of code that perform a specific task.

---

## 1. for Loop

A for loop is used to iterate over a sequence.

### Syntax

```python
for variable in sequence:
    # code
```

### Example

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

## 2. while Loop

A while loop executes as long as a condition is True.

### Syntax

```python
while condition:
    # code
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## 3. Nested Loops

A loop inside another loop is called a nested loop.

### Example

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

---

## 4. Functions

Functions are reusable blocks of code.

### Syntax

```python
def function_name():
    # code
```

### Example

```python
def greet():
    print("Hello!")

greet()
```

---

## 5. Functions with Parameters

Parameters allow data to be passed into a function.

### Example

```python
def greet(name):
    print("Hello", name)

greet("Tapaswini")
```

---

# 6. Built-in Functions

Built-in functions are functions that Python provides by default. They can be used directly without importing any module.

## print()

Used to display output.

Example:
print("Hello World")

## input()

Used to take input from the user.

Example:
name = input("Enter your name: ")

## type()

Used to check the data type of a variable.

Example:
age = 20
print(type(age))

## len()

Returns the length of a string, list, tuple, etc.

Example:
name = "Python"
print(len(name))

## range()

Generates a sequence of numbers.

Example:
for i in range(1, 6):
    print(i)

## max()

Returns the largest value.

Example:
print(max(10, 20, 30))

## min()

Returns the smallest value.

Example:
print(min(10, 20, 30))

## sum()

Returns the sum of values.

Example:
numbers = [10, 20, 30]
print(sum(numbers))

## Advantages of Built-in Functions

* Reusability
* Better code organization
* Easier debugging
* Reduces code duplication

---

## Summary

Today I learned:

* for Loop
* while Loop
* Nested Loops
* Functions
* Functions with Parameters
* print()
* input()
* type()
* len()
* range()
* max()
* min()
* sum()


Loops help repeat tasks efficiently, while functions help organize and reuse code and Built-in functions make Python programming easier and more efficient.