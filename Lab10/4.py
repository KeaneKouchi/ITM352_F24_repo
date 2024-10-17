# Read the json file of taxi trip data at  
# https://drive.google.com/file/d/1-MpDUIRZxhFnN-rcDdJQMe_mcCSciaus/view?usp=sharing 
# and create a dataframe from it. Print summary statistics about the dataframe, 
# as well as the median.

# Keane Kouchi
# 10/16/24

import pandas as pd

resultsDF = pd.read_json("Taxi_Trips.json")
print(resultsDF.describe())
print(resultsDF.head(10))

print("The median fare value is: ", resultsDF["fare"].median())