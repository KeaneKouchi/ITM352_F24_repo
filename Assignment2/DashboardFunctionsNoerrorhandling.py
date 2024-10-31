import pandas as pd
import time
#import json
#import pyarrow
import sys

####################
# Non menu item functions

def LoadCSV(url):
    print(f"Loading data from the following URL {url}")
    StartLoad = time.time()
    try:
        data = pd.read_csv(url, on_bad_lines="skip").convert_dtypes(dtype_backend="pyarrow")
        EndLoad = time.time()
        LoadTime = EndLoad - StartLoad
        print(f"Data loaded successfully in {LoadTime:.2f} seconds.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        exit()

def CheckRequiredFields(data, RequiredFields):
    MissingFields = [field for field in RequiredFields if field not in data.columns]
    if MissingFields:
        print(f"Warning: Missing required fields: {', '.join(MissingFields)}")
        print("Some analytics may not work correctly.")

def MenuSelection(MenuItems):
    while True:
        print("Please choose a category.")
        for index, menu in enumerate(MenuItems, start=1):
            print(f"{index}: {menu}")
        
        #print(f"{len(MenuItems) + 1}: Exit")  # Exit option
        
        # Get user input
        try:
            MenuChoice = int(input("Response: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
        
        if MenuChoice < 1 or MenuChoice > len(MenuItems) + 1:
            print(f"Invalid input, please choose from 1 to {len(MenuItems) + 1}.")
            continue
        
        #if MenuChoice == len(MenuItems) + 1:
        #    print("Exiting menu.")
        #    return None  # or any other exit signal you prefer
        
        ChoiceIndex = MenuChoice - 1
        print(f"You selected \"{MenuItems[ChoiceIndex]}\". \n")
        return ChoiceIndex  # Return the index of the selected item

########################
# Menu item functions, number corresponds to item number in menu

def One_ShowFirstNRows(data):
    while True:
        UserInput = input("Enter number of rows to display (or type \"all\" to display all rows): ")
    
        if UserInput.lower() == "all":
            print(data, "\n")  # Display all rows
        else:
            try:
                n = int(UserInput)
                print(data.head(n), "\n")  # Display the first n rows
            except ValueError:
                print("Invalid input. Please enter a valid number or \"all\". \n")
        return

def Two_TotalSales_Region_OrderType(data):
    data["sale_price"] = data["quantity"] * data["unit_price"]

    TotalSales_Region_OrderTypePivot = data.pivot_table(
        values="sale_price", index="sales_region", columns="order_type",
        aggfunc="sum", margins=True, margins_name="Total Sales"
    )
    return print(TotalSales_Region_OrderTypePivot, "\n")

def Three_AverageSales_Region_State_OrderType(data):
    data["sale_price"] = data["quantity"] * data["unit_price"]

    AverageSales_Region_State_OrderType_Pivot = data.pivot_table(
        values="sale_price", index="sales_region", columns=["order_type", "customer_state"],
        aggfunc="mean", margins=True, margins_name="Averages"
    )
    return print(AverageSales_Region_State_OrderType_Pivot, "\n")

def Four_Sales_CustomerType_OrderType_State(data):
    data["sale_price"] = data["quantity"] * data["unit_price"]

    Sales_CustomerType_OrderType_State_Pivot = data.pivot_table(
        values="sale_price", index="customer_state", columns=["customer_type", "order_type"],
        aggfunc="sum"  # margins = True, margins_name = "Total Sales"
    )
    return print(Sales_CustomerType_OrderType_State_Pivot, "\n")

def Five_TotalSales_Quantity_Region_ProduceName(data):
    data["sale_price"] = data["quantity"] * data["unit_price"]
    
    TotalSales_Quantity_Region_ProduceName_Pivot = data.pivot_table(
        values=["quantity", "sale_price"], index="sales_region", columns="produce_name", 
        aggfunc="sum", margins=True, margins_name="Total"
    )
    
    return print(TotalSales_Quantity_Region_ProduceName_Pivot, "\n")

def Six_TotalSales_Quantity_OrderType_CustomerType(data):
    data["sale_price"] = data["quantity"] * data["unit_price"]
    
    TotalSales_Quantity_OrderType_CustomerType_Pivot = data.pivot_table(
        values=["quantity", "sale_price"], index="order_type", columns="customer_type", 
        aggfunc="sum", margins=True, margins_name="Total"
    )
    
    return print(TotalSales_Quantity_OrderType_CustomerType_Pivot, "\n")

def Seven_Max_Min_Sales_Category(data):
    data["sale_price"] = data["quantity"] * data["unit_price"]
    
    Max_Min_Sales_Category_Pivot = data.pivot_table(
        values="sale_price", index="product_category", aggfunc=[max, min]  # margins=True, margins_name="Totals"
    )
    
    return print(Max_Min_Sales_Category_Pivot, "\n")

def Eight_Employees_Region(data):
    # temporarily remove dollar sign format
    DollarSign = pd.get_option("display.float_format")
    pd.set_option("display.float_format", None)
    Employees_Region_Pivot = data.pivot_table(
        values="employee_id", index="sales_region", aggfunc=pd.Series.nunique, 
        margins=True, margins_name="Total Unique Employees"
    )
    Employees_Region_Pivot.columns = ["Employees"]
    return print(Employees_Region_Pivot, "\n"), pd.set_option("display.float_format", DollarSign)

def Nine_CustomPivotTable(data):
    # Define available fields for each option
    data["sale_price"] = data["quantity"] * data["unit_price"]

    row_options = {
        1: "employee_name",
        2: "sales_region",
        3: "product_category"
    }
    column_options = {
        1: "order_type",
        2: "customer_type"
    }
    value_options = {
        1: "quantity",
        2: "sale_price"
    }
    agg_options = {
        1: "sum",
        2: "mean",
        3: "count"
    }

    # User selects rows
    print("Select rows (which field(s) should group the data):")
    for key, value in row_options.items():
        print(f"{key}. {value}")
    row_selection = input("Enter the number(s) of your choice(s), separated by commas: ")
    selected_rows = [row_options[int(num)] for num in row_selection.split(",") if num.strip().isdigit()]

    # User selects columns
    print("\nSelect columns (optional):")
    for key, value in column_options.items():
        print(f"{key}. {value}")
    column_selection = input("Enter the number(s) of your choice(s), separated by commas (enter for no grouping): ")
    selected_columns = [column_options[int(num)] for num in column_selection.split(",") if num.strip().isdigit()] if column_selection else []

    # User selects values
    print("\nSelect values (numeric fields to analyze):")
    for key, value in value_options.items():
        print(f"{key}. {value}")
    value_selection = input("Enter the number(s) of your choice(s), separated by commas: ")
    selected_values = [value_options[int(num)] for num in value_selection.split(",") if num.strip().isdigit()]

    # User selects aggregation function
    print("\nSelect aggregation function:")
    for key, value in agg_options.items():
        print(f"{key}. {value}")
    agg_selection = input("Enter the number(s) of your choice(s), separated by commas: ")
    selected_agg = [agg_options[int(num)] for num in agg_selection.split(",") if num.strip().isdigit()]

    # Validate selections
    if not selected_rows or not selected_values or not selected_agg:
        print("Error: You must select at least one row, one value, and one aggregation function.")
        return

    # Create the pivot table
    pivot_table = data.pivot_table(
        values=selected_values,
        index=selected_rows,
        columns=selected_columns,
        aggfunc=selected_agg,
        fill_value=0
    )

    # Display the pivot table
    print("\nGenerated Pivot Table:\n", pivot_table)

def Ten_MedianSalePriceByRegion(data):
    # Calculate sale price for each transaction
    data["sale_price"] = data["quantity"] * data["unit_price"]
    
    # Group by sales region and calculate the median sale price
    median_sale_price = data.groupby("sales_region")["sale_price"].median().reset_index()
    
    # Rename the columns for clarity
    median_sale_price.columns = ["Sales Region", "Median Sale Price"]
    
    # Display the results
    print("Median Sale Price by Sales Region:\n", median_sale_price)
    
    return median_sale_price

def Eleven_ChangeDateRange(data, original_data):
    # Ensure the 'order_date' column is in datetime format
    data["order_date"] = pd.to_datetime(data["order_date"])
    original_data["order_date"] = pd.to_datetime(original_data["order_date"])
    
    original_min_date = original_data["order_date"].min()
    original_max_date = original_data["order_date"].max()

    # Show the available date range
    print(f"Maximum date range: {original_min_date.date()} to {original_max_date.date()}")

    choice = input("Do you want to revert to the maximum date range? (yes) or choose new dates? (no): ").strip().lower()
    
    if choice == "yes":
        print("Resetting to original data.")
        return original_data.copy()  # Return a copy of the original data

    # Ask the user for new date range
    start_date = input(f"Enter start date (YYYY-MM-DD) [default: {original_min_date.date()}]: ") or str(original_min_date.date())
    end_date = input(f"Enter end date (YYYY-MM-DD) [default: {original_max_date.date()}]: ") or str(original_max_date.date())

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filter the data based on the selected date range
    filtered_data = data[(data["order_date"] >= start_date) & (data["order_date"] <= end_date)]
    
    print(f"Filtered data from {start_date.date()} to {end_date.date()}.")
    return filtered_data

def ExitProgram():
    print("Exiting the dashboard.")
    sys.exit()

