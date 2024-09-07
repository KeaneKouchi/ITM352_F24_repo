# Ask the user to input a temperature in degrees Fahrenheit.
# Convert that temperature to Celsius and output it.
# Name: Keane Kouchi
# Date: 9/4/24

degreesF = input("Please enter a temperature in Fahrenheit: ")

degreesC = (float(degreesF) - 32)*(5/9)

print("You entered:",degreesF)
print("This converts to", degreesC, "Celsius")