#Debugging exercise # 6
# Write code that will iterate through numbers from 1 to 10 and print the number if 
# it is not equal to 5 (using continue) and stop the loop entirely and print a message 
# when it reaches 8 (using break).


# changed range to start at 1 and end at 10
for x in range(1,11):
    # changed to == so it skips 5
    if x == 5:
        continue
    if x == 8:
        print("done!")
        break
    print(x)

