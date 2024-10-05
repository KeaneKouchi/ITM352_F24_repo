#Debugging exercise # 7
# Algorithm for multiplying two numbers

def multiply(x, y):
   # initialized product as 0 instead of x
   product = 0
   # changed the x variable to num
   for num in range(y):
       # adding instead of multiplying
       product += x
    # return product not y
   return product

# changed both input variables to ints
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
prod = multiply(first, second)

print(f"The product of {first}, {second} is {prod}")
