# 0.  Install matplotlib and create a first simple visualization. Use this line in your code to import matplotlib:
# import matplotlib.pyplot as plt
#
# Keane Kouchi
# 11/22/24


import matplotlib.pyplot as plt

# a. Define a list of x values and y values.  The lists should be the same length.
x_values = [1, 2, 3, 4, 5]
y_values = [1, 3, 3, 3.5, 4]

# b. Plot these values as a line graph.
plt.plot(x_values, y_values)

# c.Plot these values as a scatter plot.
plt.scatter(x_values, y_values)

# d. Add a second set of X and Y values and add these to the plot as a line graph.
other_x = [1, 2, 3, 4]
other_y = [2, 4, 6, 8]
plt.plot(other_x, other_y)

# e. Add a title and axis labels.
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Line and Scatter Plot")

plt.show()