# Open the URL https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410 
# and note the table of interest rate data. 
# Keane Kouchi
# 10/30/24

import urllib.request
import ssl
import pandas as pd
import pyarrow

# a. Use .read_html() to extract the interest rate table information 
# as a DataFrame and print out its columns. You will need to install the lxml library.  
# Set ssl._create_default_https_context = ssl._create_unverified_context
ssl._create_default_https_context = ssl._create_unverified_context
pd.set_option("display.max_columns", None)

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410"
encoding = "utf-8"

print(f"Opening {url}...")

try:
    tables = pd.read_html(url)
    int_rate_table = tables[0]
    print(int_rate_table.columns)
    print(int_rate_table.head())

# b.Use .iterrows() to loop through the the rows and print out the 1 mo interest rates

    for index, row in int_rate_table.iterrows():
        print(f"Index: {index}: 1 month rate: {row["1 Mo"]}")

except Exception as e:
    print(f"An error has occured: {e}")
