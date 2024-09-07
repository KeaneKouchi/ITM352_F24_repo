# Ask the user to input a temperature in degrees Fahrenheit.
# Convert that temperature to Celsius and output it.
# Name: Keane Kouchi
# Date: 9/4/24

def FtoC(degreesF):
    degreesC = (float(degreesF) - 32)*(5/9)
    return(degreesC)

degreesF = input("Please enter a temperature in Fahrenheit: ")


print("You entered:",degreesF)
print("This converts to", FtoC(degreesF), "Celsius")