# # LISTS
# months = ["Jan", "Feb", "Mar"]
# # pos       0      1      2

# #ACCESSING
# print(months) # entire list
# print(months[1]) # value at index 1 - Feb

# # UPDATING
# months[0] = "Dec"
# print(f"Update: {months}")

# # ADDING
# # append - adds at the end of list
# months.append("Apr")
# print(f"Append: {months}")

# # insert - adds at a specific index in a list
# months.insert(1, "January")
# print(f"Insert: {months}")

# # DELETE
# # remove - deletes the first instance of a value
# # months.remove("Oct") # ERROR since 'Oct' is not in the list.
# months.remove("Feb")
# print(f"Remove: {months}")

# # NOTE: You can check if value exist first using 'in' before remove()
# # if "Oct" in months:
# #     months.remove("Oct")
# # else:
# #     print("Oct is not in the list.")

# # pop - deletes by index
# popped_item = months.pop(1)
# print(f"{popped_item} has been deleted!")
# print(f"Pop: {months}")

# # NOTE: You can restore popped values using 'insert'.
# # months.insert(1, popped_item)
# # print(f"Restored using insert: {months}")

# # del - keyword, deletes by accessing
# del months[1]
# print(f"Del: {months}")


# NESTED LISTS:
# - lists inside another list.
# Syntax:
# months = ["Jan", "Feb", "Mar", 18, 3.14, True, []]

# grocery = [
#     ["Bawang",      2],     # row 0
#     ["Sibuyas",     25],    # row 1
#     ["Itlog",       3]      # row 2
# #    col 0        col 1
# ]
# print(grocery) # entire list
# print(grocery[0]) # entire row 0
# print(grocery[2]) # entire row 2

# ACCESING ITEMS:
# Syntax:
# variable_name[row][col]
# grocery = [
#     ["Bawang",      2,       20],     # row 0
#     ["Sibuyas",     25,      125],    # row 1
#     ["Itlog",       3,       30]      # row 2
# #    col 0        col 1     col 2
# ]
# # row             0                       1                  2
# grocery = [["Bawang", 2, 20], ["Sibuyas", 25, 125], ["Itlog", 3, 30]]
# # col          0      1   2      0        1    2        0     1   2

# print(grocery[0][0]) # Bawang
# print(grocery[2][1]) # 3
# print(grocery[1][0]) # Sibuyas
# print(grocery[2][2]) # 30

# text = f"Buy {grocery[1][0]}: {grocery[1][1]} pcs for {grocery[1][2]} pesos."
# print(text)

classmates = [
    ["Sean",    "Ensomo"],      # row 0
    ["Michael", "Espejo"],      # row 1
    ["Jhumar",  "Felasol"]      # row 2
# col   0          1
]
# print(classmates[row_index][col_index])
print(classmates[1][1]) # Espejo
print(classmates[-1][-1]) # Felasol
# print(classmates[2][2]) # ERROR

# UPDATING NESTED LIST ITEMS:
classmates = [
    ["Sean",    "Ensomo"],      # row 0
    ["Michael", "Espejo"],      # row 1
    ["Jhumar",  "Felasol"]      # row 2
# col   0          1
]
print(f"Original row 0: {classmates[0]}")
print(f"Original row 1: {classmates[1]}")
print(f"Original row 2: {classmates[2]}")

classmates[1][0] = "Michael Anndrei" # "Michael" -> "Michael Anndrei"
classmates[0][0] = "Sean Gabriel" # "Sean" -> "Sean Gabriel"
classmates[2] = "ML" #

print(f" Updated row 0: {classmates[0]}") # row 0
print(f" Updated row 1: {classmates[1]}") # row 1
print(classmates[2])

# ADDING NESTED LIST ITEMS
classmates = [
    ["Sean",    "Ensomo"],      # row 0
    ["Michael", "Espejo"],      # row 1
    ["Jhumar",  "Felasol"]      # row 2
# col   0          1
]
# append()
classmates[1].append("Jardillo")
print(classmates)

# insert()
classmates[0].insert(1, "Gunda")
print(classmates)

# DELETE NESTED LIST ITEMS:
classmates = [
    ["Sean",    "Ensomo"],      # row 0
    ["Michael", "Espejo"],      # row 1
    ["Jhumar",  "Felasol"]      # row 2
# col   0          1
]

# remove
# classmates.remove(["Michael", "Espejo"])
classmates[1].remove("Espejo")
print(classmates)

classmates = [
    ["Sean",    "Ensomo"],      # row 0
    ["Michael", "Espejo"],      # row 1
    ["Jhumar",  "Felasol"]      # row 2
# col   0          1
]
# pop
deleted_item = classmates.pop(2)
print(f"{deleted_item} has been deleted.")

removed_item = classmates[0].pop(1)
print(f"{removed_item} has been deleted.")

print(classmates)

classmates = [
    ["Sean",    "Ensomo"],      # row 0
    ["Michael", "Espejo"],      # row 1
    ["Jhumar",  "Felasol"]      # row 2
# col   0          1
]

# del
# del classmates # delete the entire list.
del classmates[2][0] #
