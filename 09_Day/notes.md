# Day 9 - Modules

## Introduction

A Module is a Python file that contains functions, variables, and classes that can be reused in other Python programs.

Modules help organize code and avoid repetition.

---

## 1. Importing a Module

Use the `import` keyword to use a module.

### Example

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

---

## 2. Built-in Modules

Python provides many built-in modules.

### math Module

Used for mathematical operations.

```python
import math

print(math.sqrt(16))
print(math.pi)
```

Common Functions:

* math.sqrt()
* math.pow()
* math.pi
* math.factorial()

---

### random Module

Used to generate random values.

```python
import random

print(random.randint(1, 10))
```

Common Functions:

* random.randint()
* random.choice()
* random.random()

---

## 3. Custom Modules

You can create your own module.

### helper.py

```python
def greet(name):
    print("Hello,", name)
```

### main.py

```python
import helper

helper.greet("Tapaswini")
```

---

## Advantages of Modules

* Code Reusability
* Better Organization
* Easier Maintenance
* Reduced Code Duplication

---

## Real-Life Uses

* Machine Learning Libraries
* Data Analysis Tools
* Web Development Frameworks
* Automation Scripts

Examples:

* NumPy
* Pandas
* Matplotlib
* TensorFlow

---

## Summary

Today I learned:

* What is a Module
* import Statement
* Built-in Modules
* math Module
* random Module
* Custom Modules

Modules help divide large programs into smaller, reusable, and manageable files.
