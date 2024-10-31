# Read a file from a url and write a local file containing just
# the first 10 rows of data

# Keane Kouchi
# 10/23/2024

import pandas as pd
import time
import json
import pyarrow

url = "https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
# import the data file. This needs to be downloaded to be used by pandas.
def LoadCSV(url):
    print("Loading data from the file...")
    StartLoad = time.time()
    try:
        data = pd.read_csv(url, on_bad_lines = "skip",dtype_backend = "pyarrow")
        EndLoad = time.time()
        LoadTime = EndLoad - StartLoad
        print(f"Data loaded successfully in {LoadTime:.2f} seconds.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        exit()

SalesData = LoadCSV(url)
SalesData.head(5130).to_csv("SalesData.csv")