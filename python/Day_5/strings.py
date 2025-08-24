# Today we are going to learn about string 

# multi line string
story = """
Once upon a time, there was a 
king who had three beautiful horses with names:
1. Gon
2. Killua
3. Hisoka
"""
print(story)

# Escape character
story = "Once upon a time, there was a \nking who had three beautiful horses with names:"
print(story)

story = "Once upon a time, there was a \tking who had three beautiful horses with names:"
print(story)

story = "Once upon a time, there was a \"king\" who had three beautiful horses with names:"
print(story)

story = "Once upon a time, there was a \'king\' who had three beautiful horses with names:"
print(story)

## String Manupulations
# counting the characters in the string
Name = "Sadiq Tech Solutions"
print(len(Name))

# string indexing
Phone_number = "dlkddjl"
print("1.",    type(Phone_number))
if Phone_number.isnumeric():
    Phone_number = int(Phone_number)
    print("2.",type(Phone_number))

print("3.",type(Phone_number))