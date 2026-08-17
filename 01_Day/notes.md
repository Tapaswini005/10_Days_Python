# Day 1 - Python Basics

## Introduction

Python is a high-level, interpreted, and beginner-friendly programming language. It is widely used in web development, data analysis, artificial intelligence, machine learning, automation, and many other fields.

----

## 1. Python Syntax

Syntax refers to the rules for writing Python code correctly.

### Example

```python
print("Hello, World!")
```

### Key Points

* Python is case-sensitive.
* Indentation is important in Python.
* No semicolon (`;`) is required at the end of statements.
* Comments are written using `#`.

### Example

```python
# This is a comment
print("Welcome to Python")
```

---

## 2. Variables

Variables are containers used to store data values.

### Creating Variables

```python
name = "Tapaswini"
age = 20
cgpa = 8.5
```

### Rules for Naming Variables

* Must start with a letter or underscore (`_`).
* Cannot start with a number.
* Can contain letters, numbers, and underscores.
* Variable names are case-sensitive.

### Valid Examples

```python
student_name = "Tapaswini"
_age = 20
marks1 = 95
```

### Invalid Examples

```python
1name = "Tapaswini"
student-name = "Tapaswini"
```

---

## 3. Data Types

Data types define the type of data stored in a variable.

### Integer (int)

Stores whole numbers.

```python
age = 20
```

### Float (float)

Stores decimal numbers.

```python
height = 5.4
```

### String (str)

Stores text enclosed in quotes.

```python
name = "Tapaswini"
```

### Boolean (bool)

Stores True or False values.

```python
student = True
```

### List

Stores multiple values in a single variable.

```python
fruits = ["Apple", "Banana", "Mango"]
```

### Tuple

Ordered collection that cannot be modified.

```python
numbers = (1, 2, 3)
```

### Dictionary

Stores data in key-value pairs.

```python
student = {
    "name": "Tapaswini",
    "age": 20
}
```

### Set

Stores unique values.

```python
unique_numbers = {1, 2, 3, 4}
```

---

## 4. Checking Data Types

The `type()` function is used to check the data type of a variable.

### Example

```python
age = 20
print(type(age))
```

Output:

```python
<class 'int'>
```

---

## 5. Taking User Input

The `input()` function is used to take input from the user.

### Example

```python
name = input("Enter your name: ")
print("Hello", name)
```

### Converting Input Types

By default, input is stored as a string.

```python
age = int(input("Enter your age: "))
```

```python
height = float(input("Enter your height: "))
```

---

## Summary

Today I learned:

* Python Syntax
* Variables
* Rules for Variable Naming
* Basic Data Types
* Using the `type()` Function
* Taking User Input


These concepts form the foundation of Python programming and are essential before learning conditionals, loops, functions, and advanced topics.
