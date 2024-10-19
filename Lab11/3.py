# 3.Add to the program you created in 2 by adding in sub-columns showing 
# the average sales by state and by sale type (retail or wholesale). 
# Set the Panda option format the output with only 2 decimals using  
# "display.float_format", "${:,.2f}".format

# Keane Kouchi
# 10/18/24

import pandas as pd

url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

try:
    SalesData = pd.read_csv(url, on_bad_lines = "skip").convert_dtypes(dtype_backend = "pyarrow")
except:
    print("Error: this is not a valid file")  

SalesData["order_date"] = pd.to_datetime(SalesData["order_date"], format = "mixed")

pd.set_option("display.max_columns", None)

# Create a pivot table
pivot = SalesData.pivot_table(
    values = "sale_price", index = "customer_state", columns = ["customer_type","order_type"],
    # Average
    aggfunc = "mean"
)

# Format ouptput with only 2 decimal places
pd.set_option("display.float_format", "${:,.2f}".format)

print(SalesData.head(5))
print("\nPivot Table:\n", pivot)