# 5. Use the requests package to create a REST query that returns the count of licenses by driver_type. 
# Here is the query that will retrieve this information and return a string of JSON 
# Keane Kouchi
# 11/1/24


import requests
import pandas as pd

url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"

# a.Make a GET request to above URL and use .json() to convert the response to records. 
# Print out the response.
response = requests.get(url)
data = response.json()
print(data)

# b.Convert the records to a data frame, set the columns to "count" and "driver_type". 
# Set the index to "driver_type" and print out the data frame.
df = pd.DataFrame(data)
df.columns = ["driver_type", "count"]
df.set_index('driver_type', inplace=True)

print(df)
