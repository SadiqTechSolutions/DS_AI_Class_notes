# Today we are going to learn typecasting in python
# Typecasting is the process of converting one data type to another data type

# int() - integer
# float() - float
# str() - string
# bool() - boolean

# Type casting from string to integer
str_num = "123"
print(str_num)
print(type(str_num))

int_num = int(str_num)
print(int_num)
print(type(int_num))

float_num = float(str_num)
print(float_num)
print(type(float_num))

bool_num = bool(str_num)
print(bool_num)
print(type(bool_num))

# Type casting from integer to string
int_num = 123
print(int_num)
print(type(int_num))

str_num = str(int_num)
print(str_num)
print(type(str_num))

# Type casting bool to integer
bool_num = True
int_num = int(bool_num)
print(int_num)
print(type(int_num))

# Type casting bool to float
bool_num = True
float_num = float(bool_num)
print(float_num)
print(type(float_num))

# Type casting bool to string
bool_num = True
str_num = str(bool_num)
print(str_num)
print(type(str_num))

"""
Example 
Task:
1. Create a dicionary of some data containing 6 data types: int, float, bool, str, list, tuple
2. Print the dictionary
3. Access the values using keys
4. Print the data type of each entry
"""

# Task 1 - Create a dictionary
College_data = {
    "Name": "Sadiq Tech Solutions",
    "Year": 2025,
    6 : "Data Science",
    "Avg_lpa": 6.5,
    "gov_recognized": True,
    "Courses": ["Data Science", "Machine Learning", "Deep Learning"],
    "Fees": (10000, 20000, 30000)
}

# Task 2 - Print the dictionary
print(College_data)
print(type(College_data))

# Task 3 - Access the values using keys
print("Name:", College_data["Name"])
print("Year:", College_data["Year"])
print("6:", College_data[6])
print("Avg_lpa:", College_data["Avg_lpa"])
print("gov_recognized:", College_data["gov_recognized"])
print("Courses:", College_data["Courses"])
print("Fees:", College_data["Fees"])

# Task 4 - Print the data type of each entry
print(type(College_data["Name"]))
print(type(College_data["Year"]))
print(type(College_data[6]))
print(type(College_data["Avg_lpa"]))
print(type(College_data["gov_recognized"]))
print(type(College_data["Courses"]))
print(type(College_data["Fees"]))



a = 2
b = 3
c = a + b
print(c)

year = 2025
print(year)
print(type(year))

greeting = "The year is"
print(greeting)
print(type(greeting))

message = greeting + " " + str(year)
print(message)
print(type(message))