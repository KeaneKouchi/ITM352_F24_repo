# 3. Create a scatter plot of fares and tips from the file “Trips_Fri07072017T4 trip_miles gt1.json”.
#
# Keane Kouchi
# 11/22/24

import matplotlib.pyplot as plt
import pandas as pd

trips_df = pd.read_json("Trips_Fri07072017T4 trip_miles gt1.json")

fares_series = trips_df.fare 
tips_series = trips_df.tips 

fig = plt.figure()

plt.plot(fares_series, tips_series, marker='.', linestyle="none")
plt.title("Tips by Fare")

# a. Put the fare on the X axis and tips on the Y axis.
plt.xlabel("Fare in $")
plt.ylabel("Tips in $")

plt.savefig("FaresXTips.png", dpi=300)

plt.show()