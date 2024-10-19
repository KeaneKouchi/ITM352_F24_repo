# 2.Adding to the program you created in 1. Create a pivot table out of this data, 
# aggregating sales by region, with columns defined by order_type 
# (which is either Retail or Wholesale). You will need to create a sales column 
# from the quantity and unit_price columns (sales = quantity * price)
#  before creating the pivot table.

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
    values = "sale_price", index = "sales_region", columns = "order_type",
    aggfunc = "sum", margins = True, margins_name = "Totals"
)

print(SalesData.head(5))
print("\nPivot Table:\n", pivot)