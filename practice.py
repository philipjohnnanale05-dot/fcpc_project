# EXAMPLE
# GUMAWA NG PROGRAM NA MAG CHECHECK KUNG PASADO AND STUDENT

grade = float(input("Enter your grade: "))

if grade >= 75:
    print ("You are Passed")
    if grade != 75:
        print ("You are failed")
    else:
        print ("Better luck nextime")
else:
    print ("Failed")