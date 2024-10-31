import pandas as pd
import time
import sys


#########################
# Non menu item functions
#########################
def LoadCSV(url):
    print(f"Loading data from the following URL: {url}")
    StartLoad = time.time()
    try:
        data = pd.read_csv(url, on_bad_lines="skip").convert_dtypes(dtype_backend="pyarrow")
        data.fillna(0, inplace = True) 
        EndLoad = time.time()
        LoadTime = EndLoad - StartLoad
        print(f"Data loaded successfully in {LoadTime:.2f} seconds.")
        return data
    except FileNotFoundError:
        print(f"Error: The file at {url} was not found.")
        exit()
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        exit()
    except Exception as e:
        print(f"Error loading data: {e}")
        exit()


def CheckRequiredFields(data, RequiredFields):
    print("Checking for required data fields...")
    MissingFields = [field for field in RequiredFields if field not in data.columns]
    if MissingFields:
        print(f"Warning: Missing required fields: {', '.join(MissingFields)}")
        print("Some analytics may not work correctly.")
    else:
        print("\nAll required fields are present.\n")


# ChatGPT with prompt: modify to make the valid inputs numbers that correspond to index positions
# but display it starting at 1 instead of 0 (pasted old code that had letter choices)
def MenuSelection(MenuItems):
    while True:
        print("--- Sales Data Dashboard ---")
        for index, menu in enumerate(MenuItems, start=1):
            print(f"{index}: {menu}")

        try:
            MenuChoice = int(input("Response: "))
        except ValueError:
            print("Invalid input, please enter a number. \n")
            continue

        if MenuChoice < 1 or MenuChoice > len(MenuItems):
            print(f"Invalid input, please choose from 1 to {len(MenuItems)}. \n")
            continue
        
        ChoiceIndex = MenuChoice - 1
        print(f"You selected \"{MenuItems[ChoiceIndex]}\".\n")
        return ChoiceIndex

# ChatGPT but prompt is below, was connected to function 9(custom pivot) but put this half here because
# this function is technically not a dashboard menu function on its own
def selectMultipleOptions(options: dict, prompt: str, allow_empty: bool = False) -> list:
    print(prompt)
    for key, value in options.items():
        print(f"{key}. {value}")
    selection = input("Enter the number(s) of your choice(s), separated by commas: ")
    
    if selection.strip() == "" and allow_empty:
        return []

    selected = []
    for num in selection.split(","):
        num = num.strip()
        if num.isdigit() and int(num) in options:
            selected.append(options[int(num)])
        else:
            print(f"Invalid selection: {num}. Please choose valid options.")
    
    if not allow_empty and not selected:
        print(f"You must select at least one option from 1 to {len(options)}.\n")
        return selectMultipleOptions(options, prompt, allow_empty)

    return selected

#####################
# Menu item functions
#####################

# ChatGPT with prompt
# Modify my code (copy and pasted) to return to the dashboard menu if user presses enter
# and start the row number at 1 instead of the index position
def One_ShowFirstNRows(data):
    while True:
        print(f"There are {len(data)} available rows.")
        print("Enter rows to display:")
        print(f"- Enter a number from 1 to {len(data)}")
        print("- To see all rows, enter 'all'")
        print("- To skip preview, press Enter")
        
        UserInput = input("Your choice: ")

        if UserInput.lower() == "all":
            print(data, "\n")
            return  
        elif UserInput == "":
            print("Skipping preview...\n")
            return  

        else:
            try:
                n = int(UserInput)
                if n < 1 or n > len(data):
                    print(f"Number must be between 1 and {len(data)}.\n")
                    continue
                
                # Display the first n rows, adjusting the index display
                displayed_data = data.head(n)
                displayed_data.index = range(1, n + 1)  # Adjust index to start from 1
                print(displayed_data, "\n")
                return  

            except ValueError:
                print("Invalid input. Please enter a valid positive number or \"all\". \n")


def Two_TotalSales_Region_OrderType(data):
    try:
        data["sale_price"] = data["quantity"] * data["unit_price"]

        TotalSales_Region_OrderTypePivot = data.pivot_table(
            values = "sale_price", index = "sales_region", columns = "order_type",
            aggfunc = "sum", margins = True, margins_name = "Total Sales"
        )
        print(TotalSales_Region_OrderTypePivot, "\n")
    except Exception as e:
        print(f"Error calculating total sales: {e}")


# altered the format above and asked ChatGPT to modify the code using the following prompt:
# "Modify this to show both categories of order type (retail/wholesale) in columns directly 
# next to each other for each state"
def Three_AverageSales_Region_State_OrderType(data):
    try:
        data["sale_price"] = data["quantity"] * data["unit_price"]
        data.fillna(0, inplace=True)

        AverageSales_Region_State_OrderType_Pivot = data.pivot_table(
            values = "sale_price", index = "sales_region", columns = ["customer_state", "order_type"],
            aggfunc = "mean", margins = True, margins_name = "Average Sales"
        )
        # displays retail and wholesale by state in adjacent columns
        AverageSales_Region_State_OrderType_Pivot.columns = [f"{state} - {order_type}" 
        for state, order_type in AverageSales_Region_State_OrderType_Pivot.columns]
        
        print(AverageSales_Region_State_OrderType_Pivot, "\n")

    except Exception as e:
        print(f"Error calculating average sales: {e}")


def Four_Sales_CustomerType_OrderType_State(data):
    try:
        data["sale_price"] = data["quantity"] * data["unit_price"]

        Sales_CustomerType_OrderType_State_Pivot = data.pivot_table(
            values = "sale_price", index = "customer_state", columns = ["customer_type", "order_type"],
            aggfunc = "sum"
        )
        print(Sales_CustomerType_OrderType_State_Pivot, "\n")
    except Exception as e:
        print(f"Error calculating sales: {e}")

# ChatGPT with prompt: Modify to convert the values in quantity column to an int and
# make NA values into 0: copy and pasted my code
def Five_TotalSales_Quantity_Region_ProduceName(data):
    try:
        data["sale_price"] = data["quantity"] * data["unit_price"]
        
        TotalSales_Quantity_Region_ProduceName_Pivot = data.pivot_table(
            values=["quantity", "sale_price"], index = "sales_region", columns = "produce_name",
            aggfunc = "sum", margins = True, margins_name = "Total"
        )
        
        # convert the quantities to int to keep it from being formatted with $
        if "quantity" in TotalSales_Quantity_Region_ProduceName_Pivot.columns:
            TotalSales_Quantity_Region_ProduceName_Pivot["quantity"] = TotalSales_Quantity_Region_ProduceName_Pivot["quantity"].fillna(0).astype(int)

        print(TotalSales_Quantity_Region_ProduceName_Pivot, "\n")
    
    except Exception as e:
        print(f"Error calculating total sales quantity: {e}")


def Six_TotalSales_Quantity_OrderType_CustomerType(data):
    try:
        data["sale_price"] = data["quantity"] * data["unit_price"]

        TotalSales_Quantity_OrderType_CustomerType_Pivot = data.pivot_table(
            values = ["quantity", "sale_price"], index = "order_type", columns = "customer_type", 
            aggfunc = "sum", margins = True, margins_name = "Total"
        )
        if "quantity" in TotalSales_Quantity_OrderType_CustomerType_Pivot.columns:
            TotalSales_Quantity_OrderType_CustomerType_Pivot["quantity"] = TotalSales_Quantity_OrderType_CustomerType_Pivot["quantity"].fillna(0).astype(int)
        print(TotalSales_Quantity_OrderType_CustomerType_Pivot, "\n")
    except Exception as e:
        print(f"Error calculating total sales quantity by order type: {e}")

def Seven_Max_Min_Sales_Category(data):
    try:
        data["sale_price"] = data["quantity"] * data["unit_price"]
        Max_Min_Sales_Category_Pivot = data.pivot_table(
            values = "sale_price", index = "product_category", aggfunc = [max, min]
        )
        print(Max_Min_Sales_Category_Pivot, "\n")
    except Exception as e:
        print(f"Error calculating max/min sales by category: {e}")


def Eight_Employees_Region(data):
    try:
        Employees_Region_Pivot = data.pivot_table(
            values = "employee_id", index = "sales_region", aggfunc = pd.Series.nunique, 
            margins = True, margins_name = "Total Unique Employees"
        )
        Employees_Region_Pivot.columns = ["Employees"]
        if "Employees" in Employees_Region_Pivot.columns:
            Employees_Region_Pivot["Employees"] = Employees_Region_Pivot["Employees"].fillna(0).astype(int)
        print(Employees_Region_Pivot, "\n")

    except Exception as e:
        print(f"Error calculating employees per region: {e}")

# ChatGPT with prompt: Generate a function called Nine_CustomPivotTable that creates a custom
# pivot table following these instructions (copy and pasted from Assignment2 instructions)
# I reprompted probably 20 separate times to include data validation and specifically
# to get it to accept pressing enter as a valid input for only the one time it's optional

def Nine_CustomPivotTable(data: pd.DataFrame) -> None:
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

    selected_rows = selectMultipleOptions(row_options, "Select rows (which field(s) should group the data):")
    selected_columns = selectMultipleOptions(column_options, "Select columns (optional- press enter to skip):", allow_empty=True)
    selected_values = selectMultipleOptions(value_options, "Select values (numeric fields to analyze):")
    selected_agg = selectMultipleOptions(agg_options, "Select aggregation function:")

    try:
        pivot_table = data.pivot_table(
            values=selected_values, index=selected_rows, columns=selected_columns,
            aggfunc=selected_agg, fill_value=0
        )
        print("\nGenerated Pivot Table:\n", pivot_table)
    
    except Exception as e:
        print(f"Error generating pivot table: {e}")


# ChatGPT with prompt: create a function in the same format as ones previous called 
# Ten_MedianSalePrice_State that shows median sales by customer_state. Make it start at 1 
# instead of the index position
def Ten_MedianSalePrice_State(data):
    try:
        data["sale_price"] = data["quantity"] * data["unit_price"]
        median_sale_price = data.groupby("customer_state")["sale_price"].median().reset_index()
        median_sale_price.columns = ["Sales Region", "Median Sale Price"]
        median_sale_price.index = range(1, len(median_sale_price) + 1)
        print("Median Sale Price by State:\n", median_sale_price)
        return median_sale_price
    except Exception as e:
        print(f"Error calculating median sale price by region: {e}")


# ChatGPT with prompt: Generate a function called Eleven_ChangeDateRange that prompts the user
# to enter a start and end date of data they want to analyze. Keep the date range for all analysis
# until the user chooses to manually change the date range. 
# I had to re prompt it a few times to handle data validation (date format, dates within range)
def Eleven_ChangeDateRange(data, original_data):
    try:
        # Convert order_date to datetime
        data["order_date"] = pd.to_datetime(data["order_date"])
        original_data["order_date"] = pd.to_datetime(original_data["order_date"])
        
        original_min_date = original_data["order_date"].min()
        original_max_date = original_data["order_date"].max()

        # Loop until valid start date is entered
        while True:
            print(f"Available dates: {original_min_date.date()} -> {original_max_date.date()}")
            print("Note: Chosen date range will remain constant for all analysis until changed again")
            start_date_input = input(f"Enter start date (YYYY-MM-DD) [default: {original_min_date.date()}]: ") or str(original_min_date.date())
            try:
                start_date = pd.to_datetime(start_date_input)
                
                # Check if the start date is within the original range
                if start_date < original_min_date or start_date > original_max_date:
                    print(f"Start date must be between {original_min_date.date()} and {original_max_date.date()}.")
                    continue  
                    
                break  
            except ValueError:
                print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")

        # Loop until valid end date is entered
        while True:
            end_date_input = input(f"Enter end date (YYYY-MM-DD) [default: {original_max_date.date()}]: ") or str(original_max_date.date())
            try:
                end_date = pd.to_datetime(end_date_input)
                
                # Check if the end date is within the original range
                if end_date < original_min_date or end_date > original_max_date:
                    print(f"End date must be between {original_min_date.date()} and {original_max_date.date()}.")
                    continue  
                    
                break 
            except ValueError:
                print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")

        # Filter the data based on the selected date range
        filtered_data = data[(data["order_date"] >= start_date) & (data["order_date"] <= end_date)]
        print(f"Filtered data from {start_date.date()} to {end_date.date()}.")
        return filtered_data
    
    except Exception as e:
        print(f"An error occurred while changing the date range: {e}")


def ExitProgram():
    print("Exiting the dashboard.")
    sys.exit()