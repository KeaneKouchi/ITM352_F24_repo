# 1. Create a histogram from the trip miles data found in the file “Trips from area 8.json”.    
#
# Keane Kouchi
# 11/22/24

# a.	Use trip miles as the X axis and frequency as the Y axis.
import pandas as pd
import matplotlib.pyplot as plt

trips_df = pd.read_json("Trips from area 8.json")

trip_miles_series = trips_df.trip_miles

# fig = plt.figure()

plt.hist(trip_miles_series)
plt.title("Distribution of Trip Miles")

# a. Use trip miles as the X axis and frequency as the Y axis.
plt.xlabel("Trip Miles")
plt.ylabel("Frequency")

plt.show()