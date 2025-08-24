# variable is used to store information
# now we are going to declare three variables

name = "Fyzan"
age = 21
height = 5.9
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# local variable
def local():
    loc_var = "local variable"
    print(loc_var)

local()

# print(loc_var)  # This will cause an error because loc_var only exists inside local()

# global variable
glob_var = "global variable"

def show_global():
    print(glob_var)

show_global()
