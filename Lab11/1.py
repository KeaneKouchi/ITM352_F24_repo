# Read in a CSV file with sales data, called sales_data.csv, and print the first 5 rows.
# The file can be found here:https://drive.google.com/file/d/1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K/view?usp=drive_link 

# Keane Kouchi
# 10/18/24

import pandas as pd

url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

# a.Read the CSV file using exception handling and convert the data types 
# using the pyarrow data type backend. Have it skip bad lines read in. 

try:
    SalesData = pd.read_csv(url, on_bad_lines = "skip").convert_dtypes(dtype_backend = "pyarrow")
except:
    print("Error: this is not a valid file")  

# b. Use Pandas to convert the order_date column into a standard date representation. 
SalesData["order_date"] = pd.to_datetime(SalesData["order_date"], format = "mixed")

# c. Set the Panda option "display.max_columns", None, to force the display of all columns. 
pd.set_option("display.max_columns", None)

print(SalesData.head(5))


