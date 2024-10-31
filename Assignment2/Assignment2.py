# Assignment2- I am assigned additional requirements 5 and 7
# 5.Implement a new non-trivial sales analytic (simple variations of existing analytics 
# would not satisfy this requirement). 
# 7.Before performing an analysis, ask the user what date range of sales data to use. 
# Use only that range for the analysis.

# Keane Kouchi
# 10/30/24

import pandas as pd
import json
import DashboardFunctions as DF


# URL of the sales data file
URL = 'https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA'

# List of required fields for the analytics dashboard
RequiredFields = ['order_type', 'sales_region', 'customer_state', 'customer_type','quantity',
                'unit_price', 'produce_name', 'product_category', 'employee_id']

# Load the data
SalesData = DF.LoadCSV(URL)

SalesData["order_date"] = pd.to_datetime(SalesData["order_date"], format="mixed")

OriginalSalesData = SalesData.copy()


# Display the number of rows and available columns
print(f"Number of rows: {len(SalesData)}")
print(f"Available columns: {list(SalesData.columns)}")

# Check for required fields
DF.CheckRequiredFields(SalesData, RequiredFields)

# Display options
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
SalesData.fillna(0, inplace=True)
pd.set_option("display.float_format", "${:,.2f}".format)

# ChatGPT with prompt: modify to treat item as the listed dashboard menu item and function as the function
# name to be called. 
with open('DashboardMenu.json', 'r') as file:
    DASHBOARDMENU = json.load(file)
    MenuItems = [item['item'] for item in DASHBOARDMENU['DashboardMenu']]
    MenuFunctions = {item['item']: getattr(DF, item['function']) for item in DASHBOARDMENU['DashboardMenu']}

while True:
    SelectedIndex = DF.MenuSelection(MenuItems)
    if SelectedIndex is None:
        break

    SelectedFunction = MenuFunctions.get(MenuItems[SelectedIndex])
    if SelectedFunction is DF.Eleven_ChangeDateRange:
        SalesData = SelectedFunction(SalesData, OriginalSalesData)
    # Necessary to exclude the exit function from using SalesData by default
    elif SelectedFunction is DF.ExitProgram:
        SelectedFunction()
    elif callable(SelectedFunction):
        SelectedFunction(SalesData)
    else:
        print(f"Error: No valid function associated with {SelectedIndex}.")
