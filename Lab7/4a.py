# Write a Python program that will iterate through the list sample_fares = [8.60, 5.75, 13.25, 21.21] 
# and print a message “This fare is high!” if the fare is greater than 12 dollars and “This fare is low” otherwise.
# Name: Keane Kouchi
# Date: 9/27/24

SampleFares = [8.60, 5.75, 13.25, 21.21]

for fares in SampleFares:
    if fares > 12: print(f"The fare of ${fares:.2f} is high!")
    else: print(f"The fare of ${fares:.2f} is low.")


# 4b list in the loop
#for fares in [8.60, 5.75, 13.25, 21.21]:
#    if fares > 12: print(f"The fare of ${fares:.2f} is high!")
#    else: print(f"The fare of ${fares:.2f} is low.")