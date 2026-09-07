# String formatting : f Formatting strings using variables.

words = "D."
output = f"Hello, {words}!"
print (output)

Celsius = input("Enter the temperature in Celsius: ")
Celsius = float(Celsius)
Fahrenheit = Celsius * (9/5) + 32

print (f"The temperature in {Celsius}°C is {Fahrenheit}°F in Fahrenheit.")
