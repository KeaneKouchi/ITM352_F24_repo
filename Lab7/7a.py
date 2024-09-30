# Write code that will iterate through numbers from 1 to 10 
# and print the number if it is not equal to 5 (using continue) 
# and stop the loop entirely and print a message when it reaches 8 (using break).

# Keane Kouchi
# 9/27/24

UserInput = input("Enter a number: ")

for Number in range(1,11):
    if Number == 5:
        continue
    if Number == 8:
        print("8:Loop stopped")
        break
    print(Number)



# experimenting
#for Number in {1, 2, 3, 4, 5, UserInput, 6, 7, 8, 9, 10}:
#    if Number == 5:
#        continue
#    if type(Number) is str:
#        continue
#    if Number == 8:
#        print("8:Loop stopped")
#        break
#    print(Number)