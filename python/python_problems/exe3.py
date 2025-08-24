user_input = input("Enter a String: ")
print(f"{user_input} is a string")


# Method 1 using enumerate
for i,a in enumerate(user_input):
    if i % 2 == 0:
        print(a)

# Method 2 using range len and index
for i in range(len(user_input)):
    if i % 2 == 0:
        print(user_input[i])

# Method 3 using range step
for i in range(0,len(user_input),2):
    print(user_input[i])

# Method 4 using list
user_str = user_input[0:len(user_input):2]
print(type(user_str))
for i in user_str:
    print(i)