# Write a Python program that will iterate through the list sample_fares = [8.60, 5.75, 13.25, 21.21] 
# and print a message “This fare is high!” if the fare is greater than 12 dollars and “This fare is low” otherwise.
# this time using a function and test cases
# Name: Keane Kouchi
# Date: 9/27/24


def FareCheck(fares):
    for fare in fares:
        if fare > 12: print(f"This fare of ${fare:.2f} is high!")
        else: print(f"This fare of ${fare:.2f} is low.")
    return

#SampleFares = [8.60, 5.75, 13.25, 21.21]

TestCases = [
    # to test a $0 fare
    [8.60, 5.75, 13.25, 21.21, 0],
    # to test a negative
    [8.60, 5.75, 13.25, 21.21, -1],
    # to test a non decimal
    [8.60, 5.75, 13.25, 21.21, 1],
    # to test an empty list
    [],

    #expected to have errors
    # to test a tuple in the list
    [8.60, 5.75, 13.25, 21.21, (1,)],
    # to test a string in the list
    [8.60, 5.75, 13.25, 21.21, "a"]

]

for case in TestCases:
    print("\nTesting case:", case)
    FareCheck(case)

    # experimenting
    if case: print("Works!")