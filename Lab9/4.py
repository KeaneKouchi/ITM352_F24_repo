# Modify the program in Exercise 3 to calculate the total of all fares, 
# the average of those fares, and the maximum trip distance 
# (based on the Trip Miles field) for records that have fares greater than 10 dollars.
# Name: Keane Kouchi
# Date: 10/9/24

import csv

FaresTotal = 0
FaresCount = 0
MaxTripDistance = 0

with open("taxi_1000.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    
    Fares = header.index("Fare")
    TripMiles = header.index("Trip Miles")

    for row in reader:
        fare = float(row[Fares])
        TripDistance = float(row[TripMiles])

        if fare > 10:
            FaresTotal += fare
            FaresCount += 1
            MaxTripDistance = max(MaxTripDistance, TripDistance)

FaresAverage = FaresTotal / FaresCount

print(f"Total Fares: ${FaresTotal:.2f}")
print(f"Average fare: ${FaresAverage:.2f}")
print(f"Maximum distance: {MaxTripDistance} miles")