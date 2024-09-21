# 
# 
# Name: Keane Kouchi
# Date: 9/20/24

TripDurations = [1.1, 0.8, 2.5, 2.6]
TripFares = ("$6.25", "$5.25", "$10.50", "$8.05")

TripsDict = {
    "Miles": TripDurations,
    "Fares": TripFares,

}

# used for 3.7a
# print(TripsDict)

# used for 3.7b
print(f"The third duration is {TripsDict["Miles"][2]} miles")
print(f"The third cost is {TripsDict["Fares"][2]}")