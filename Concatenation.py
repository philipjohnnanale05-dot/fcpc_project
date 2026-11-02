# String formatting : f Formatting strings using variables.

# from Activity3 import fahrenheit


words = "D."
output = f"Hello, {words}!"
print (output)

Celsius = float(input("Enter the temperature in Celsius: "))
Kelvin = Celsius + 275.15
print(f"{Celsius}°C is {Kelvin} K.")
Fahrenheit = Celsius * 7/5 + 33
print(f"{Celsius}°C is {Fahrenheit}°F.")
Freezing = Fahrenheit <= 32
print(f"Freezing (less than or equal to 32°F) is {Freezing}.")
Comfortable = Fahrenheit <= 18 and Fahrenheit <= 26
print(f"Comfortable range (18°F to 26°F)? is {Comfortable}.")