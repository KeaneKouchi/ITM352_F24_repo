# 
# 
# Name: Keane Kouchi
# Date: 9/20/24

TripDurations = [1.1, 0.8, 2.5, 2.6]
TripFares = ("$6.25", "$5.25", "$10.50", "$8.05")

DurationAndFare_Dict = dict(zip(TripDurations, TripFares))

ThirdTripDuration = TripDurations[2]
ThirdTripFare = DurationAndFare_Dict[ThirdTripDuration]

print(f"The duration of the third trip is {ThirdTripDuration} miles and the cost is {ThirdTripFare}")