# Day 2 - Python Conditionals

## Introduction

Conditionals allow a program to make decisions based on certain conditions. They help the program execute different blocks of code depending on whether a condition is True or False.

---

## 1. if Statement

The `if` statement executes a block of code only when the condition is True.

### Syntax

```python
if condition:
    # code to execute
```

### Example

```python
age = 20

if age >= 18:
    print("You can vote")
```

### Output

```text
You can vote
```

---

## 2. if-else Statement

The `if-else` statement is used when there are two possible outcomes.

### Syntax

```python
if condition:
    # code if condition is True
else:
    # code if condition is False
```

### Example

```python
age = 16

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
```

### Output

```text
You cannot vote
```

---

## 3. if-elif-else Statement

The `if-elif-else` statement is used when multiple conditions need to be checked.

### Syntax

```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
```

### Example

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

### Output

```text
Grade B
```

---

## 4. Comparison Operators

Comparison operators compare two values and return either True or False.

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not Equal to             |
| >        | Greater than             |
| <        | Less than                |
| >=       | Greater than or Equal to |
| <=       | Less than or Equal to    |

### Example

```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
```

### Output

```text
False
True
False
True
```

---

## 5. Logical Operators

Logical operators are used to combine multiple conditions.

### AND Operator

Returns True only if both conditions are True.

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry Allowed")
```

### OR Operator

Returns True if at least one condition is True.

```python
age = 16
has_permission = True

if age >= 18 or has_permission:
    print("Entry Allowed")
```

### NOT Operator

Reverses the result.

```python
is_raining = False

if not is_raining:
    print("Go outside")
```

---

## Real-Life Applications of Conditionals

* Login Systems
* ATM Machines
* Online Shopping Discounts
* Student Grade Calculation
* Voting Eligibility Check
* Game Development

---

## Summary

Today I learned:

* if Statement
* if-else Statement
* if-elif-else Statement
* Comparison Operators
* Logical Operators (and, or, not)

Conditionals help programs make decisions based on different situations and are one of the most important concepts in Python programming.
