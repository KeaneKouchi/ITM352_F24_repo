# Use the Python csv module to calculate the average, maximum, and minimum values for 
# the REALINC field that have a value greater than 0 in the survey_1000.csv file. 
# Also report the number of values for the REALINC field that are greater than 0. 
# Hint: The REALINC field is the 5,457th field in the CSV file. 

# Name: Keane Kouchi
# Date: 10/9/24

import csv

RealINCsum = 0
RealINCcount = 0
RealINCmaximum = float('-inf')
RealINCminimum = float('inf') 

with open('survey_1000.csv', 'r') as csvfile:
    survey = csv.reader(csvfile)
    next(survey)

    for row in survey:
        RealINC = float(row[5456])

        if RealINC > 0:
            RealINCsum += RealINC
            RealINCcount += 1
            RealINCmaximum = max(RealINCmaximum, RealINC)
            RealINCminimum = min(RealINCminimum, RealINC)
        
RealINCaverage = RealINCsum / RealINCcount

print(f"Count of REALINC values greater than 0: {RealINCcount}")
print(f"Average of REALINC: {RealINCaverage}")
print(f"Maximum value in REALINC: {RealINCmaximum}")
print(f"Minimum value in REALINC: {RealINCminimum}")