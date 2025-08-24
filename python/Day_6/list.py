items = ["apple", "banana", "cherry"]
num_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
more_items = ["orange", "grapes", "mango"]

# append adds the list as a single element, it does not unpack the list
num_items.append(more_items)
print(num_items)

# extend unpacks the list and adds each element to the list
num_items.extend(more_items)
print(num_items)

# insert adds the element at the specified index
num_items.insert(1, "kiwi")
print(num_items)

# remove removes the specified element
num_items.remove("kiwi")
print(f"After remove: {num_items}")

# pop removes the element at the specified index
num_items.pop(5)
print(f"After pop: {num_items}")

# clear removes all elements from the list and makes it empty
# num_items.clear()
print(f"After clear: {num_items}")

# del list[index] removes the element at the specified index
del num_items[5]
print(f"After del: {num_items}")


# copy copies the list
new_num_items = num_items.copy()
print(f"After copy: {new_num_items}")

# count counts the number of times an element appears in the list
num_items.count("apple")
print(f"After count: {num_items}")

# tuple converts the list to a tuple
num_items_tuple = tuple(num_items)
print(type(num_items_tuple))
print(num_items_tuple)