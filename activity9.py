# LISTS
# ordered, changeable collection of values
# Syntax:
# variable_name = ["value1", "value2", "value3", ...]
# Lists enclosed by square brackets[]
# Objects/values inside the list is called items or elements
# Items are separated by commas(,)
# for example:
# toyo, suka, meat, paminta, laurel, onion, garlic
ingredients = ["toyo", "suka", "meat", "paminta", "laurel", "onion", "garlic"]
grade_equivalent = [4.00, 3.00, 2.00, 1.00]
my_info = ["Philip John Nanale", 29, 1.66, True]
my_list = [] # empty list
print(type(ingredients)) # <class 'list'>
print(ingredients)

# ACCESS LIST ITEMS:
# INDEX - unique number assigned to each item based on their location in the list
# fruits = ["apple", "banana", "cherry", "durian"]
# positive. index: 0, 1, 2, 3
# negative. index: -4, -3, -2, -1
# cheat sheet
# positive index, left to right - uses 0 and above
# negative index, right to left - uses -1 and below
# print (variable_name[index])
# print (fruits[3]) # durian
# print (fruits[1]) # banana
# NOTE: Indexing starts at 0, not 1, index 0 is always the first item/element in the list.
# index -1 is always the last item/element in the list.

# len() - len is short for length, it counts the number of items/elements in the list
# example:
# row1 = ["angeles", "arizabal", "bernardo", "chan", "ednalgan", "emeterio"]
# print(len(row1)) # 6

# empty = []
# print(len(empty)) # 0

# in strings, len() counts the number of characters in the string.
# example:
#school = "FCPC"
# print(len(school)) # 4
# section = "BSIT CS 1A"
# print(len(section)) # 10

# MUTABLE AND IMMUTABLE:
# Mutable: changeable, can be modified after creation
# Immutable: unchangeable, cannot be modified after creation
# example:
# list is mutable
# string is immutable

# MODIFY LIST ITEMS:
# change the value of an item in the list

# ADDING ITEMS TO THE LIST:
# append() - always add the new item at the end of the list.
# Syntax:
# variable_name.append("new_value")
# tropa.append("lazaro") [... "ocmer", "lazaro"]
# tropa.append("ibasco") [... "ocmer", "lazaro", "ibasco"]
# print(tropa)
# tropa = ["angela", "arizabal", "bernardo", "chan", "ednalgan", "emeterio"]
# add "fernandez" to the list
# tropa.append("fernandez")
# print(tropa) # ["angela", "arizabal", "bernardo", "chan", "ednalgan", "emeterio", "fernandez"]

# insert(index, new_value) - add a new value on a specific index.
# Syntax:
# variable_name.insert(target_index, "new_value")
# enemy,insert(2, "espejo")
# add "fernandez" to the list at a specific index
# tropa.insert(0, "fernandez")
# print(tropa) # ["fernandez", "angela", "arizabal", "bernardo", "chan", "ednalgan", "emeterio"]
# add multiple items to the list
# tropa.extend(["fernandez", "garcia", "herrera"])
# print(tropa) # ["fernandez", "angela", "arizabal", "bernardo", "chan", "ednalgan", "emeterio", "fernandez", "garcia", "herrera"]
# add a list to the list
# tropa.extend(["fernandez", "garcia", "herrera"])
# print(tropa) # ["fernandez", "angela", "arizabal", "bernardo", "chan", "ednalgan", "emeterio", "fernandez", "garcia", "herrera"]

# pop(index) - delete items by index.popped items can be stored in
# NOTE: pop() without index deletes the last element/item.
# Syntax:
# variable_name.pop(index)
# or
# storage_name = variable_name.pop(index)
