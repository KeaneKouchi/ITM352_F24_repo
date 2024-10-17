# Use zip() to creat a list of (age,gender) tuples
# Using Pandas, convert the list to a DataFrame, 
# with names as the index and columns Age and Gender.
# Print out the dataframe and summarize the DataFrame using the describe() method.
# Calculate and print out the average age by gender


# Keane Kouchi
# 10/16/24

import pandas as pd

# List of individuals' ages
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]

#Lists of individuals' names and genders
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

# a.Use zip() create a list of (age, gender) tuples.  
dict = zip(ages, gender)

# b.Using Pandas, convert the list to a DataFrame, with names as the index 
# and columns Age and Gender. Print out the dataframe and summarize the DataFrame 
# using the describe() method.
df = pd.DataFrame(dict, columns=["Age","Gender"], index = names)

print(df)
summary = df.describe()
print(summary)

# c.Calculate and print out the average age by gender
AverageAgeByGender = df.groupby("Gender")["Age"].mean()
print(AverageAgeByGender)