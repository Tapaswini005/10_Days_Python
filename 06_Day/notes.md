# Day 6 - Dictionaries and Sets

## Introduction

Dictionaries and Sets are important Python data structures used for storing collections of data.

---

## 1. Dictionaries

A Dictionary stores data in key-value pairs.

### Features

* Ordered
* Mutable (can be modified)
* Does not allow duplicate keys

### Example

```python id="m6iksp"
student = {
    "name": "Tapaswini",
    "age": 20,
    "branch": "CSE AIML",
    "roll no.": 24
}
```

### Accessing Values

```python id="s9pjlwm"
print(student["name"])
```

Output:

```text id="vktnux"
Tapaswini
```

---

## 2. Dictionary Methods

### keys()

Returns all keys.

```python id="hj0xvk"
print(student.keys())
```

### values()

Returns all values.

```python id="zq2e8q"
print(student.values())
```

### items()

Returns key-value pairs.

```python id="b8lcfj"
print(student.items())
```

### update()

Adds or updates values.

```python id="8rhhg7"
student.update({"city": "Kolkata"})
```

---

## 3. Sets

A Set is an unordered collection of unique elements.

### Features

* Unordered
* Mutable
* No duplicate values allowed

### Example

```python id="1p6e7s"
numbers = {1, 2, 3, 4}
```

---

## 4. Set Methods

### add()

Adds an element.

```python id="86h4p0"
numbers.add(5)
```

### remove()

Removes an element.

```python id="e2u2ga"
numbers.remove(2)
```

### union()

Combines two sets.

```python id="hjlwm1"
set1 = {1, 2}
set2 = {3, 4}

print(set1.union(set2))
```

### intersection()

Returns common elements.

```python id="2v2uvj"
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.intersection(set2))
```

---

## Difference Between Dictionary and Set

| Dictionary                 | Set                          |
| -------------------------- | ---------------------------- |
| Stores key-value pairs     | Stores unique values         |
| Uses {} with key:value     | Uses {} with values only     |
| Access by key              | No indexing                  |
| Duplicate keys not allowed | Duplicate values not allowed |

---

## Summary

Today I learned:

* Dictionaries
* Dictionary Methods
* Accessing Dictionary Values
* Sets
* Set Methods
* Difference Between Dictionary and Set

Dictionaries are useful for storing related information using keys, while Sets are useful for storing unique values and performing set operations.
