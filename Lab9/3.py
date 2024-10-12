# Read the 1,000 lines of taxi data from the taxi_1000.csv file and calculate the total of all fares, 
# the average of those fares, and the maximum trip distance (based on the Trip Miles field).
# 
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

        FaresTotal += fare
        FaresCount += 1
        MaxTripDistance = max(MaxTripDistance, TripDistance)

FaresAverage = FaresTotal / FaresCount

print(f"Total Fares: ${FaresTotal:.2f}")
print(f"Average fare: ${FaresAverage:.2f}")
print(f"Maximum distance: {MaxTripDistance} miles")