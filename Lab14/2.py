# 2. Create a second histogram from the trip miles data found in the file "Trips from area 8.json".
#
# Keane Kouchi
# 11/22/24

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

trips_df = pd.read_json("Trips from area 8.json")

# b. Drop rows with NA values.
trips_df = trips_df.dropna()

trips_df = trips_df[['tips', 'payment_type']]
trips_df = trips_df.astype({'tips': float})
trips_df = trips_df.set_index('payment_type')

tips_by_payment_type = trips_df.groupby('payment_type').sum()

# a. Use payment method as the X axis and (sum of) tips as the Y axis.
x_labels = pd.Series(tips_by_payment_type.index.values)
y_values = pd.Series(tips_by_payment_type['tips'].values)

bars = np.array(range(len(x_labels)))
plt.xticks(bars, x_labels, color='red', fontweight='bold')

plt.bar(bars, y_values)

# c. Assign appropriate labels and a title to the plot.
plt.title("Taxi Tips by Payment Type")
plt.xlabel("Payment Type")
plt.ylabel("Tips in $")
plt.show()





