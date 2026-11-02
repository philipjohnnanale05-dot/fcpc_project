# CONDITIONAL EXECUTION/STATEMENTS
# - this is the heart of decision-making of your programs
# - a code block gets executed depending whether condition is True or False.
# Syntax:

# condition = False
# if condition:
#     print("This is inside 'if' statement.")
#     print("Condition is True.")
# else:
#     print("This is inside 'else' statement.")
#     print("Condition is False.")

# print("This is outside 'if-else' statement.")

# age = 15

# if age >= 18:
#     print("You may vote.")
# else:
#     print("You are not old enough yet.")

# if
# - is always the first part of the conditional statement.
# - code under 'if' is executed when condition is True.

# elif
# - is always after the 'if' statement.
# - code under 'elif' is executed when preceeding 'if' is False.

# else - (fallback, last option)
# - is always the last part of the conditional statement.
# - code under 'else' is executed when NO 'if' condition is True.

# age = int(input("Enter age: "))

# if (age >= 13) and (age <= 19): # Teenage is 13 - 19
#     print("You are a teenager.")
# else:
#     print("You are NOT a teenager!")

grade = 79

if grade >= 90 and grade <= 100: # grade 90-100: 1.00
#   75 >= 90          75 <= 100  
#       F      and        T  = False
    print(f"Your grade, {grade}, is 1.00!")

elif grade >= 80 and grade <= 89: # grade 80-89: 2.00
    print(f"Your grade, {grade}, is 2.00!")

elif grade >= 75 and grade <= 79: # grade 75-79: 3.00
    print(f"Your grade, {grade}, is 3.00!")

else: # grade <74: Failed
    print(f"Your grade, {grade}, is a failing grade.")
    print("See you next sem! :>")

# 1, 2
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

# 3
bmi = weight / (height ** 2)

# 4
print(f"Your BMI is: {bmi}")
print("============================")

if bmi < 18.5: # underweight: bmi < 18.5
    print(f"You bmi, {bmi}, is underweight.")
    print(f"You bmi, {bmi}, is underweight.")
    print(f"You bmi, {bmi}, is underweight.")
    print(f"You bmi, {bmi}, is underweight.")
    print(f"You bmi, {bmi}, is underweight.")
    print(f"You bmi, {bmi}, is underweight.")
    print(f"You bmi, {bmi}, is underweight.")
    print(f"You bmi, {bmi}, is underweight.")
    print(f"You bmi, {bmi}, is underweight.")
    print(f"You bmi, {bmi}, is underweight.")
    print(f"You bmi, {bmi}, is underweight.")

elif (bmi >= 18.5) and (bmi <= 24.9): # normal: bmi 18.5 - 24.9
    print(f"You bmi, {bmi}, is normal.")

elif (bmi >= 25.0) and (bmi <= 29.9): # overweight: bm 25.0 - 29.9
    print(f"You bmi, {bmi}, is overweight.")

else: # obese: bmi >= 30.0
    print(f"You bmi, {bmi}, is obese.")