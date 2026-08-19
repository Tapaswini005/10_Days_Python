# Day 3 - Type Casting and Exceptions

## Introduction

When working with different data types, sometimes we need to convert one data type into another. This process is called Type Casting.

Exceptions are errors that occur during program execution. Python provides exception handling to prevent programs from crashing.

---

## 1. Type Casting

Type Casting is the process of converting one data type into another.

### Example

```python
age = "20"
age = int(age)

print(age)
print(type(age))
```

Output:

```text
20
<class 'int'>
```

---

## 2. Implicit Type Casting

Python automatically converts one data type into another when needed.

### Example

```python
num1 = 10
num2 = 5.5

result = num1 + num2

print(result)
print(type(result))
```

Output:

```text
15.5
<class 'float'>
```

---

## 3. Explicit Type Casting

The programmer manually converts data types using functions such as:

* int()
* float()
* str()
* bool()

### Example

```python
num = "100"

print(int(num))
print(float(num))
print(str(num))
```

---

## Common Type Casting Functions

| Function | Description         |
| -------- | ------------------- |
| int()    | Converts to Integer |
| float()  | Converts to Float   |
| str()    | Converts to String  |
| bool()   | Converts to Boolean |

---

## 4. Exceptions

Exceptions are errors that occur while a program is running.

### Example

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError
```

---

## 5. try-except Block

Used to handle exceptions gracefully.

### Syntax

```python
try:
    # risky code
except:
    # handling code
```

### Example

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except:
    print("Invalid input or division by zero")
```

---

## Common Exceptions

| Exception         | Cause                  |
| ----------------- | ---------------------- |
| ZeroDivisionError | Dividing by zero       |
| ValueError        | Invalid value          |
| TypeError         | Wrong data type        |
| IndexError        | Invalid list index     |
| KeyError          | Invalid dictionary key |

---

## Why Exception Handling?

* Prevents program crashes
* Makes programs user-friendly
* Helps identify and handle errors properly

---

## Summary

Today I learned:

* Type Casting
* Implicit Type Casting
* Explicit Type Casting
* Exceptions
* try-except Blocks

These concepts help in handling different data types and managing errors effectively in Python programs.
