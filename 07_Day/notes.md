# Day 7 - File Handling

## Introduction

File Handling is used to store and retrieve data from files. It allows data to be saved permanently instead of being lost when the program ends.

---

## Opening a File

Syntax:

```python
file = open("filename", "mode")
```

### Common Modes

| Mode | Description     |
| ---- | --------------- |
| r    | Read File       |
| w    | Write File      |
| a    | Append Data     |
| x    | Create New File |

---

## 1. Reading a File

```python
file = open("sample.txt", "r")
print(file.read())
file.close()
```

---

## 2. Writing to a File

```python
file = open("sample.txt", "w")
file.write("Hello Python")
file.close()
```

---

## 3. Appending to a File

```python
file = open("sample.txt", "a")
file.write("New Data")
file.close()
```

---

## 4. Closing a File

```python
file.close()
```

Closing a file releases system resources.

---

## 5. Using with open()

The recommended way to work with files.

```python
with open("sample.txt", "r") as file:
    print(file.read())
```

Advantages:

* Automatically closes the file
* Cleaner code
* Safer

---

## File Methods

### read()

Reads entire file.

```python
file.read()
```

### readline()

Reads one line.

```python
file.readline()
```

### write()

Writes data.

```python
file.write("Hello")
```

---

## Real-Life Uses

* Saving student records
* Storing user information
* Log files
* Configuration files
* Data processing

---

## Summary

Today I learned:

* Opening Files
* Reading Files
* Writing Files
* Appending Data
* File Modes (r, w, a, x)
* with open()
* File Methods

File Handling allows programs to store data permanently and is widely used in real-world applications.