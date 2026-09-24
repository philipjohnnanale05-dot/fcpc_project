# # Variable initialization: create variable
# # Syntax:
# variable_name = "value"

# age = 18
# section = "BSITCS 1A"
# grade = 79.2

# print(age)
# print(section)

# # Rules in naming variables
# # 1. variable names must start with either a letter or underscore.
# age = 18
# _section = "BSITCS 1A"

# # 1styear = "BSITCS 1A" # ERROR
# # $chool = "FCPC" # ERROR

# # 2. variable names are case-sensitive. Uppercase is not the same as lowercase.
# # e.g. age != AGE
# weather = "sunny" # ALL lowercase
# Weather = "Raining" # titlecase
# WEATHER = "cloudy" # ALL uppercase

# print(weather)

# # 3. variable names can only contain letters, numbers, or underscore.
# # Simply, NO whitespaces and NO special characters (!@#$%^&*()+-={}[]:"|;'\,./<>?")
# # we@ther = "windy" # ERROR
# # first name = "Ramon Joseph" # ERROR

# # 4. variable names cannot use reserved keywords.
# # e.g. print, input, type, class, for, if, elif, else

# age = 18
# apple_count = 12
# school = "FCPC"
# generalweightedaverage = 15
# general_weighted_average = 15

# # COMMENTS are ignored when running the code
# # Single-line comments take up the entire line. (This is a single-line comment)

# # Inline comments are comments in a line alongside code.
# print("Hello world!") # says 'Hello world!' (This is an inline comment)

# Basic Input & Output:
# OUTPUT
# print() - display value sa terminal
# print("Hello world!")

# first_name = "Ramon Joseph"
# print(first_name) # Ramon Joseph

# last_name = "Verdon"
# print(first_name, last_name) # Ramon Joseph Verdon
# print(first_name, last_name, sep="-") # Ramon Joseph-Verdon
# print(first_name, last_name, sep="++") # Ramon Joseph++Verdon

# print("Your first name is", first_name) # Your first name is Ramon Joseph
# print("Your last name is", last_name) # Your last name is Verdon
# print("Your full name is", first_name, last_name) # Your full name is Ramon Joseph Verdon

# INPUT
# input() - allows user to give information to the program
# Syntax:
# variable_name = input("question/command: ")

# age = input("How old are you? ")
# age = input("Enter age: ")

# first_name = input("What is your first name? ")
# print(first_name)

# last_name = input("Enter last name: ")
# print("You entered:", last_name)

pet_name = input("What is your pet's name? ") # INPUT: bubbles
print(pet_name, "is a nice name!") # OUTPUT: bubbles is a nice name!