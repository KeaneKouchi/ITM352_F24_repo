# Create a list of tuples (provided) and convert the list into a Numpy array,
# report the dimensions of the array, the # of elements in it

# Keane Kouchi
# 10/16/24

import numpy as np

incomes = [
    (10, 14629),(20, 25600),(30, 37002),(40, 50000),(50, 63179),
    (60, 79542),(70, 100162),(80, 130000),
    (90, 184292)
]

# a. Convert the list into a Numpy Array and report the dimensions of the array and the number of elements in it.
npIncomes = np.array(incomes)

print("The dimensions of the household income array:", npIncomes.ndim)
print("The number of elements in the income array:", npIncomes.size) 

# b.Print out the table of percentiles and household incomes
for i in range(len(npIncomes)):
    print(npIncomes[i][0], npIncomes[i][1])