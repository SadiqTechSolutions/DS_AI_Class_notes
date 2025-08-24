# Today we are going to learn data types in python

height = 5.10

print(height)
print(type(height))

# Text based data types
name = "Sadiq Tech Solutions"
print("Text based data types - String")
print(type(name))

# Number based data types - Integer, Float, Complex

# Integer data type
age = 21
print("------Integer data type------")
print(type(age))

# Float data type
height = 5.10
print("------Float data type------")
print(type(height))

# Complex data type
complex_num = 1 + 2j
print("------Complex data type------")
print(type(complex_num))


# Boolean data type
is_active = True
print("------Boolean data type------")
print(type(is_active))


## Collection data types - List, Tuple, Set, Dictionary

# List data type
# Properties of list
# 1. ordered
# 2. mutable (changeable)
# 3. allows duplicate
# Syntax - Square brackets []
fruits = ["apple", 9 , 0.9, "cherry", bool(is_active)]
print("------List data type------")
print(fruits)
print(type(fruits))

# Tuple data type
# Properties of tuple
# 1. ordered
# 2. immutable (unchangeable)
# 3. allows duplicate
# Syntax - Parentheses ()
tuple_fruits = ("apple", 9, 0.9, "cherry", bool(is_active))
print("------Tuple data type------")
print(tuple_fruits)
print(type(tuple_fruits))

# Set data type
# Properties of set
# 1. unordered
# 2. mutable (changeable)
# 3. does not allow duplicate
# Syntax - Curly braces {}
set_fruits = {"apple", 9, 0.9, "cherry", bool(is_active)}
print("------Set data type------")
print(set_fruits)
print(type(set_fruits))

# Dictionary data type
# Properties of dictionary
# 1. ordered
# 2. mutable (changeable)
# 3. does not allow duplicate
# Syntax - Curly braces {}
bio_data = {"Name": "Fyzan", "Age": 21, "Height": 5.10, "is_active": True, "is_student": True, "Speciality": "Data Science"}
print("------Dictionary data type------")
print(bio_data)
print(type(bio_data))

# Accessing values in dictionary using keys
print("Name:", bio_data["Name"])
print("Age:", bio_data["Age"])
print("Height:", bio_data["Height"])
print("is_active:", bio_data["is_active"])
print("is_student:", bio_data["is_student"])
print("Speciality:", bio_data["Speciality"])