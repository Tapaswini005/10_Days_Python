# Day 8 - Object-Oriented Programming (OOP)

## Introduction

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using Classes and Objects. It helps make programs more reusable, organized, and scalable.

---

## 1. Class

A Class is a blueprint for creating objects.

### Example

```python id="8m0s5e"
class Student:
    pass
```

---

## 2. Object

An Object is an instance of a class.

### Example

```python id="e74tgi"
class Student:
    name = "Tapaswini"

student1 = Student()

print(student1.name)
```

---

## 3. Constructor

A Constructor is a special method called automatically when an object is created.

### Syntax

```python id="3tb5z6"
def __init__(self):
    pass
```

### Example

```python id="6tk1kt"
class Student:
    def __init__(self, name):
        self.name = name
```

---

## 4. Instance Methods

Methods are functions inside a class.

### Example

```python id="xw7qri"
class Student:
    def greet(self):
        print("Hello")
```

---

## 5. Inheritance

Inheritance allows one class to inherit properties and methods from another class.

### Example

```python id="tthz2q"
class Person:
    pass

class Student(Person):
    pass
```

### Benefits

* Code Reusability
* Reduced Redundancy
* Better Organization

---

## 6. Polymorphism

Polymorphism allows different classes to use methods with the same name.

### Example

```python id="8f2jyo"
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")
```

---

## Advantages of OOP

* Reusability
* Modularity
* Scalability
* Easier Maintenance
* Better Code Organization

---

## Real-Life Example

Class: Car

Objects:

* BMW
* Audi
* Tesla

Each object has:

* Color
* Speed
* Model

And methods like:

* Start()
* Stop()
* Accelerate()

---

## Summary

Today I learned:

* Class
* Object
* Constructor
* Instance Methods
* Inheritance
* Polymorphism

OOP helps create structured and reusable programs and is widely used in large software projects.
