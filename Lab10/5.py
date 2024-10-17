# 

# Keane Kouchi
# 10/16/24

import pandas as pd


# Read in a CSV file at  and turn it into a Pandas dataframe. 

dfHomes = pd.read_csv("../homes_data.csv")

# a. Print out the dimensions of the DataFrame and show the first 10 rows
shape = dfHomes.shape
print(f"The homes data has {shape[0]} rows and {shape[1]} columns")
print("First 10 rows of homes data:\n", dfHomes.head(10))

# b.Select only properties that have 500 or more units. 
# Drop some unnecessary columns and print the first 10 rows
dfBigApartments = dfHomes[dfHomes.units >= 500]
dfBigApartments = dfBigApartments.drop(columns=["id", "easement"])
print("First 10 rows of BigApartments:\n",dfBigApartments.head(10))

# c.Look at the data types. Determine which data types are incorrect 
# and coerce them to the correct data type. 
# Look at the data types now and print the cleaned data.

print(dfBigApartments.info())

dfBigApartments["land_sqft"] = pd.to_numeric(dfBigApartments["land_sqft"], errors = "coerce")
dfBigApartments["gross_sqft"] = pd.to_numeric(dfBigApartments["gross_sqft"], errors = "coerce")
dfBigApartments["sale_price"] = pd.to_numeric(dfBigApartments["sale_price"], errors = "coerce")

print(dfBigApartments.info())
print("First 10 rows of BigApartments after cleaning:\n",dfBigApartments.head(10))

# d. We have some null values and duplicates.  Drop those rows and print out the results. 

dfBigApartments = dfBigApartments.dropna()
dfBigApartments = dfBigApartments.drop_duplicates(dfBigApartments.columns, keep = "first")

print(dfBigApartments.info())
print("First 10 rows of BigApartments after cleaning and dropping:\n",dfBigApartments.head(10))

# e.Filter out 0 sales and print the results. Compute and display the average sales price 

dfBigApartments = dfBigApartments[dfBigApartments["sale_price"] > 0]

print(dfBigApartments.info())
print("After filtering out 0 sales: \n",dfBigApartments.head(10))
print("The average sales price of big apartments is: ", round(dfBigApartments["sale_price"].mean(),2))