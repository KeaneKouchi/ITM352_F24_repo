# 6. Create a 3D plot of fares, trip miles and dropoff area based on “Trips from area 8.json”. 
# To do this you will need to add this line to your code: 
# from mpl_toolkits.mplot3d import Axes3D

# Keane Kouchi
# 11/22/24

import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

trips_df = pd.read_json("Trips from area 8.json")

trips_gt_1 = trips_df[['trip_miles', 'fare', 'dropoff_community_area']].query('trip_miles > 1')

fare_series = trips_gt_1.fare
trip_miles = trips_gt_1.trip_miles
dropoff_area = trips_gt_1.dropoff_community_area

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(fare_series, trip_miles, dropoff_area, c = 'b', marker='.')

plt.title("Fares by Taxi Trip Miles and Dropoff Area")
ax.set_xlabel('Fares')
ax.set_ylabel('Trip Miles')
ax.set_zlabel('Dropoff Area')
plt.show()