age = float(input("Enter your age: "))
height = float(input("Enter your height: "))

if age >= 12:
    if height >= 140:
        print ("Big Coaster: OK")
    else:
        print ("Too short")
else:
    if height >= 120:
        print ("Junior Coaster: OK")
    else:
        print ("Not tall enough yet")