# Day 5 - Lists and Tuples

## Introduction

Lists and Tuples are Python data structures used to store multiple values in a single variable.

---

## 1. Lists

A List is an ordered and mutable collection.

### Features

* Ordered
* Changeable (Mutable)
* Allows duplicate values

### Example

```python
fruits = ["Apple", "Banana", "Mango"]
print(fruits)
```

### Accessing Elements

```python
print(fruits[0])
print(fruits[1])
```

---

## 2. List Methods

### append()

Adds an item to the end.

```python
fruits.append("Orange")
```

### remove()

Removes an item.

```python
fruits.remove("Banana")
```

### insert()

Adds an item at a specific position.

```python
fruits.insert(1, "Grapes")
```

### pop()

Removes an item by index.

```python
fruits.pop(0)
```

---

## 3. List Slicing

Used to access a range of elements.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

---

## 4. Tuples

A Tuple is an ordered and immutable collection.

### Features

* Ordered
* Cannot be modified (Immutable)
* Allows duplicate values

### Example

```python
colors = ("Red", "Green", "Blue")
```

### Accessing Elements

```python
print(colors[0])
```

---

## 5. Tuple Methods

### count()

Counts occurrences of a value.

```python
numbers = (1, 2, 2, 3)
print(numbers.count(2))
```

### index()

Returns the position of a value.

```python
print(numbers.index(3))
```

---

## Difference Between List and Tuple

| List            | Tuple              |
| --------------- | ------------------ |
| Mutable         | Immutable          |
| Uses []         | Uses ()            |
| More methods    | Fewer methods      |
| Can be modified | Cannot be modified |

---

## Summary

Today I learned:

* Lists
* Accessing List Elements
* List Methods
* List Slicing
* Tuples
* Tuple Methods
* Difference Between Lists and Tuples

Lists are useful when data needs to change, while Tuples are useful when data should remain fixed.
