# Variable Initialization
variable_name = "value"

# Rules in Naming Variables
# 1. should always start with letter or underscore
school = "FCPC"
_school = "FCPC"
# $chool = "FCPC" # ERROR

# 2. variable names are case-sensitive. Uppercase is not the same lowercase.
AGE = 18
age = 19
Age = 20

# 3. should only have letter, numbers, and underscore.
# NO SPECIAL CHARACTER AND NO WHITESPACES
# first name = "Juan" # ERROR

first_name = "Juan"
general_weighted_average = 1.25

# 4. cannot be reserved keywords.
# print, type, input, if, else, elif, and, or, etc.

# COMMENTS - preceded by #, ignored when running code
# single-line comments - takes up the entire line
# inline comments
name = "Juan" # user's name is juan (THIS IS AN INLINE COMMENT)

# BASIC INPUT & OUTPUT
# print() - OUTPUT, display value to the terminal.
# print("Hello world!")

section = "BSITCS 1A"
# print(section) # BSITCS 1A
# print("I am a", section, "student.") # I am a BSITCS 1A student.

# input() - INPUT, allows the user to input/provide information.
# Syntax:
# variable_name = input("question/prompt/command: ")
# first_name = input("Enter first name: ")

# first_name = input("What is your first name? ")
# print("Your first name is", first_name)


# DATA TYPES: the type of data a variable holds
# type() - returns the data type of a variable
# PRIMITIVE:
# 1. Integer - int, 'whole' numbers either + or -
age = 18
print("Variable (age) is", type(age))
year = -2026
print("Variable (year) is", type(year))

# 2. Float - float, numbers 'with decimal places' either + or -
temp = -37.8
print("Variable (temp) is", type(temp))
gwa = 2.5
print("Variable (gwa) is", type(gwa))

# 3. Strings - str, textual enclosed by "" or ''
name = "Ramon Joseph Verdon"
section = 'BSITCS 1A'

money_str = "1000" # string
money_int = 1000 # integer

# 4. Booleans - bool, either True or False.
is_valid = True
is_logged_in = False
pogi = False

# MODERN (COMPOSITE) - lists, tuples, dictionaries, sets
fruits = ["apple", "banana", "cherry"] # LIST

# TYPE CASTING - process of converting one data type to another
# IMPLICIT - data type is 'automatically' decided/converted
# In Python, data type is implicitly casted.
age = 18
name = "Ramon Joseph Verdon"

# EXPLICIT - data type is 'manually' decided/converted.
# In Java, data type of variable are explicitly included in syntax.
# Int age = 18;
# String name = "Ramon Joseph Verdon";
# Boolean is_valid = "true";

# CASTING FUNCTIONS:
# int() - manually converts a value to an Integer.
# base10 means 0-9
money = int("1000") # "1000"[str] -> 1000[int]
print(money / 2) # 500

currency = "10.50"
# print(int(currency) / 2) # ERROR: int() uses base10

temp = 37.999
print(int(temp)) # 37, simply get the whole number.

valid = True
print(int(valid)) # 1, True = 1; False = 0

# float() - manually converts a value to a Float.
# base10 means 0-9 and/or period (.)
currency = "10.50"
print(float(currency) + 1) # 11.5

age = float("18")
print(age) # 18.0

temp = float(100)
print(temp) # 100.0

logged_in = False
print(float(logged_in)) # 0.0, True = 1.0; False = 0.0

# str() - manually converts a value to a String.
# Commonly in 'String' Concatenation - combining 2 or more strings using +
age = str(18)
print("Variable (age) is", type(age))

money = str(5.25)
print("Variable (money) is", type(money))

jowable = str(True)
print("Variable (jowable) is", type(jowable))

first_name = "Ramon Joseph"
last_name = "Verdon"
full_name = first_name + " " + last_name
print(full_name) # Ramon Joseph Verdon

program = "BSITCS"
section = "1A"
print(program + "-" + section) # BSITCS-1A

age = 18
print("I am " + str(age) + " years old.")
#       str     str     str

# bool() - manually converts a value to a Boolean.
# In strings, it is only False if the string is empty.
name = "" # empty string
print(bool(name)) # False, empty string
print(bool("a")) # True

# In numbers (int, float), it is only False when number is 0 or 0.0
print(bool(0)) # False
print(bool(0.0)) # False

print(bool(6)) # True
print(bool(-6)) # True
print(bool(6.75)) # True
print(bool(-6.75)) # True

# input(), by defaults, takes in all input as strings.
# meter to km converter
# meter = float(input("Enter meter: "))
# km = meter / 1000 # or meter * 0.001
# print(str(meter) + " meters is " + str(km) + " km.")
# 1500 meters is 1.5 km

dollar = float(input("Enter dollar: "))
peso = dollar * 62.38
print(peso)

# F-strings - lets you call variables and do expressions inside strings
school = "FCPC"
section = "BSITCS 1A"
total_students = 40

# f-string
print(f"I study at {school} under {section}. We are {total_students} students in class.")

# string concatenation
print("I study at " + school + " under " + section + ". We are " + str(total_students) + " students in class.")

current_age = 18
greet = f"Happy Birthday! You are {age + 1} years old now!"
print(greet)

# OPERATORS - symbols that does operation
# Arithmetic (math) Operators
# 1. Addition           +
print(1 + 1) # 2

# 2. Subtraction        -
print(12 - 5) # 7

# 3. Multiplication     *
print(4 * 3) # 12

# 4. Division           / - complete division
print(87 / 4) # 21.75

# 5. Exponentiation     **
print(4 ** 3) # 4x4x4 = 64

# 6. Floor Division     // - gets the quotient
print(87 // 4) # 21

# 7. Modulus            % - gets the remainder
print(87 % 4) # 3
print(104 % 2) # 104 is even because remainder is 0
print(567 % 2) # 567 is odd because remainder is 1 or simply, there is a remainder.

# Order of Operators (Precedence)
# P - parenthesis
# E - exponentiation
# M, D - multiplication, division (include floor div, modulus)
# A, S - addition, subtraction




# Comparison (relational) Operators
# Conditional (logical) Operators

# Assginment Operator, Bitwise, etc.