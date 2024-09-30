 #Write Python code that executes a for loop that examines every element of the tuple 
 # (“hello,” 10; “goodbye,” 3; “goodnight,” 5). Within the loop, use an if statement 
 # to count how many of the elements are strings. After the loop completes, 
 # print out a message stating how many strings are in the tuple.

# Name: Keane Kouchi
# Date: 9/27/24

ValuesTuple = ("hello", 10, "goodbye", 3, "goodnight", 5)

strings = 0

for values in ValuesTuple:
    if type(values) is str:
        strings += 1  

print(f"There are {strings} strings in the tuple.")

