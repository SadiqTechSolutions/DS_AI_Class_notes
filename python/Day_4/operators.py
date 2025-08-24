# Today we are going to learn about operators in python

# Arithmatic operators
# + - addition
# - - subtraction
# * - multiplication
# / - division
# % - modulus
# ** - exponentiation
# // - floor division

# Example
a = 10
b = 20
print("========Arithmatic operators========")
print(a + b) # 1. addition
print(a - b) # 2. subtraction
print(a * b) # 3. multiplication
print(a / b) # 4. division
print(a % b) # 5. modulus
print(a ** b) # 6. exponentiation
print(a // b) # 7. floor division

# Assignment operators
# = - assignment
# += - addition assignment
# -= - subtraction assignment
# *= - multiplication assignment
# /= - division assignment
# %= - modulus assignment
# **= - exponentiation assignment
# //= - floor division assignment

# Example
a = 10
b = 20
print("========Assignment operators========")
a = a + b
a += b
print(a) # 1. addition assignment
a = a - b
a -= b
print(a) # 2. subtraction assignment
a = a * b
a *= b
print(a) # 3. multiplication assignment
a = a / b
a /= b
print(a) # 4. division assignment
a = a % b
a %= b
print(a) # 5. modulus assignment
a = a**b
a **= b
print(a) # 6. exponentiation assignment
a = a//b
a //= b
print(a) # 7. floor division assignment

# Comparison operators
# == - equal to
# != - not equal to
# > - greater than
# < - less than
# >= - greater than or equal to
# <= - less than or equal to

# Example
print("========Comparison operators========")
a = 10
b = 20
print(a == b) # 1. equal to
print(a != b) # 2. not equal to
print(a > b) # 3. greater than
print(a < b) # 4. less than
print(a >= b) # 5. greater than or equal to
print(a <= b) # 6. less than or equal to

# Logical operators
# and - logical and
# or - logical or
# not - logical not

# Example
print("========Logical operators========")
a = True
b = False
print(a and b) # 1. logical and
print(a or b) # 2. logical or
print(not a) # 3. logical not

# Example
x = 10
y = 20
print(x > y and x < y) # 1. logical and
print(x > y or x < y) # 2. logical or
print(not x > y) # 3. logical not

# Membership operators
# in - membership in
# not in - membership not in

# Example
print("========Membership operators========")
a = "Hello"
b = "World"
print("H" in a) # 1. membership in
print("W" not in b) # 2. membership not in

# Identity operators
# is - identity is
# is not - identity is not

# Example
print("========Identity operators========")
a = 10
b = 20
print(a is b) # 1. identity is
print(a is not b) # 2. identity is not


# Instructions:
# 1. Define variables for the prices of three items.

#
# 2. Calculate the subtotal of the items.
#
# 3. Define a boolean variable to represent if the customer has a membership card.
#
# 4. Determine if the customer is eligible for a discount. The discount rules are:
#    - The subtotal must be $30.00 or more, AND
#    - The customer must have a membership card.
#    Store the result (True or False) in a variable called 'is_eligible_for_discount'.
#
# 5. Calculate the final total.
#    - If the customer is eligible for a discount, apply a 10% discount (subtotal * 0.9).
#    - Otherwise, the final total is the same as the subtotal.
#    (Hint: You can use an if/else statement, which we'll cover soon, or a clever trick with
#     multiplication. For now, it's okay to calculate it as if you know the eligibility.)
#     For a challenge, try to calculate the final price without an if-statement!
#
# 6. Print all the results in a user-friendly receipt format:
#    - The price of each item.
#    - The subtotal.
#    - A message indicating if the discount was applied (e.g., "Discount Applied: True").
#    - The final total.