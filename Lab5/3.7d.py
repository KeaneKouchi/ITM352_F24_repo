# Create a list of dictionaries where each dictionary is a trip
# 
# Name: Keane Kouchi
# Date: 9/20/24

Trips = [
    {"Duration0": 1.1, "Fare0": "6.25"},
    {"Duration1": 0.8, "Fare1": "$5.25"},
    {"Duration2": 2.5, "Fare2": "$10.50"},
    {"Duration3": 2.6, "Fare3": "$8.05"},
]

ThirdTrip = Trips[2]
ThirdTripDuration = ThirdTrip["Duration2"]
ThirdTripFare = ThirdTrip["Fare2"]

print(f"The duration of the third trip is {ThirdTripDuration} miles and the cost is {ThirdTripFare}")