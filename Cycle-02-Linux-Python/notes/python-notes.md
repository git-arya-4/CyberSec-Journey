# Python Notes

## 1. Data Types in Python

Data types define the kind of value a variable can store in Python.

### Integer (`int`)

Used for whole numbers.

Example:
age = 21
roll_number = 45
print(age)

### Float (`float`)

Used for decimal numbers.

Example:
price = 99.99
temperature = 36.5
print(price)

### String (`str`)

Used to store text or characters inside quotes.

Example:
name = "Arya"
college = "KIIT"
print(name)

### Boolean (`bool`)

Stores only two values: `True` or `False`.

Example:
is_logged_in = True
print(is_logged_in)

### List (`list`)

Stores multiple values in a single variable. Lists are mutable.

Example:
marks = [85, 90, 78, 88]
print(marks)

### Tuple (`tuple`)

Similar to a list but values cannot be changed.

Example:
coordinates = (10, 20)
print(coordinates)

### Dictionary (`dict`)

Stores data in key-value pairs.

Example:
student = {
"name": "Arya",
"age": 21,
"branch": "CSE"
}
print(student)

---

## 2. Loops in Python

Loops are used to execute a block of code multiple times.

### `for` Loop

Used when the number of iterations is known.

Example:
for i in range(1, 6):
print("Number:", i)

Expected Output:
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5

### `while` Loop

Used when the loop should continue until a condition becomes false.

Example:
count = 1

```
while count <= 5:
    print(count)
    count += 1
```

Expected Output:
1
2
3
4
5

---

## 3. Functions in Python

Functions are blocks of reusable code that perform a specific task.

### Function Without Parameters

Example:
def greet():
print("Hello, welcome to Python")

```
greet()
```

### Function With Parameters

Example:
def add(a, b):
return a + b

```
result = add(10, 20)
print(result)
```

Expected Output:
30

### Function With Default Parameter

Example:
def greet_user(name="Guest"):
print("Hello", name)

```
greet_user()
greet_user("Arya")
```

---

## 4. File Handling in Python

File handling is used to create, read, write, and append data in files.

### Writing to a File

Example:
file = open("sample.txt", "w")
file.write("This is a sample file.")
file.close()

### Reading from a File

Example:
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

### Appending to a File

Example:
file = open("sample.txt", "a")
file.write("\nThis line is added later.")
file.close()

### Using `with` Statement

This is a better way because the file closes automatically.

Example:
with open("sample.txt", "r") as file:
content = file.read()
print(content)

---

## Conclusion

Python provides different data types to store values, loops to repeat tasks, functions to organize reusable code, and file handling to work with files efficiently.
