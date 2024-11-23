# 5. Create a scatter plot of fares by trip miles based on “Trips from area 8.json”.
#
# Keane Kouchi
# 11/22/24

import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("dark_background")

trips_df = pd.read_json("Trips from area 8.json")

# b. Filter out trips of 0 miles.
# trip_miles_gt_0 = trips_df[['trip_miles', 'fare']].query('trip_miles > 0')


# c. Filter out trips less than 2 miles.
trip_miles_gt_0 = trips_df[['trip_miles', 'fare']].query('trip_miles > 2')

fare_series = trip_miles_gt_0.fare 
trip_miles = trip_miles_gt_0.trip_miles

plt.plot(fare_series, trip_miles, marker="o", linestyle="none", alpha=0.3)
plt.title("Fare by Taxi Trip Miles > 2")
plt.xlabel("Fare in $")
plt.ylabel("Distance in Miles")

# a. Save the plot to a file called FaresXmiles.png
plt.savefig("FaresXMiles.2.png", dpi=300)
plt.show()