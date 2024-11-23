# 4. Create a scatter plot of fares by trip miles based on “Trips from area 8.json”.

# Keane Kouchi
# 11/22/24

import matplotlib.pyplot as plt
import pandas as pd

trips_df = pd.read_json("Trips from area 8.json")

trip_miles_gt_0 = trips_df[['trip_miles', 'fare']].query('trip_miles > 0')
fare_series = trip_miles_gt_0.fare 
trip_miles = trip_miles_gt_0.trip_miles

# b. Now create the same scatter plot using plt.plot with linestyle= "none" and marker="."
#plt.plot(fare_series, trip_miles, linestyle="none", marker=".")

# c. Now make the plot fancier, with a “v” marker, cyan color, and 0.2 transparency.
plt.plot(fare_series, trip_miles, marker="v", linestyle="none", color='c', alpha=0.2)
#plt.scatter(fare_series, trip_miles)
plt.title("Fares by Taxi Trip Miles")

# a. Put the fare on the X axis and the trip miles on the Y axis.  Use plt.scatter().
plt.xlabel("Total Fare in Dollars")
plt.ylabel("Distance in Miles")

plt.savefig("FaresXMiles.png", dpi=300)
plt.show()

