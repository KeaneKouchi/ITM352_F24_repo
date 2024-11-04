# 4. Retrieve and analyze public vehicle license data from Chicago’s open API using sodapy and pandas. 
# Use the the sodapy.Socrata client with the URL data.cityofchicago.org to get the JSON file rr23-ymwb. 
# Set the limit to fetch only the first 500 records. 
# Keane Kouchi
# 10/30/24

import pandas as PD
from bs4 import BeautifulSoup as BS
from sodapy import Socrata

client = Socrata("data.cityofchicago.org", None)
results = client.get("rr23-ymwb", limit=500)

# a.Convert the data you get to a DataFrame and inspectt the first few results. 
df = PD.DataFrame.from_records(results)
PD.set_option("display.max_columns", None)
print(df.head())

# c/b?. Use the results to print out the vehicles and fuel_sources
# Assuming the column names are 'vehicle_type' and 'fuel_source'
if "vehicle_type" in df.columns and "vehicle_fuel_source" in df.columns:
    print(df[["vehicle_type", "vehicle_fuel_source"]].drop_duplicates())

# d. Group the vehicles by fuel type and output the number of vehicles per fuel source
data = df.groupby("vehicle_fuel_source").size().reset_index(name="# of vehicles")
print(data)























#a.Convert the data you get to a DataFrame and inspectt the first few results. 

#c.Use the results to print out the vehicles and fuel_sources

#d.Group the vehicles by fuel type and output the number of vehicles per fuel source
