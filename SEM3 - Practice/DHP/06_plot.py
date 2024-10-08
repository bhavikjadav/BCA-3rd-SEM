"""
Create CSV file for Items selling for 6 months and add atleast 5 records for 5 different Items.

Create Python script to perform following task.

Read data in Dataframe.
Add columns and calculate total_sell, average_sell.
Plot Total sell and average sell together on bar chart with proper Legends, titles and labels.
Explain final dataframe to csv named sell_analyasis.csv
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Getting data from CSV
data = pd.read_csv("data.csv")
print(data)

data['total_sell'] = data['quantity_sold'] * data['price']
data['average_sell'] = data['total_sell'] / data['quantity_sold']
print(data)

bar_width = 0.35  # Width of the bars
x = np.arange(len(data['item_name']))  # The label locations

bars1 = plt.bar(x - bar_width/2, data['total_sell'], width=bar_width, label='Total Sell', color='skyblue')
bars2 = plt.bar(x + bar_width/2, data['average_sell'], width=bar_width, label='Average Sell', color='orange')

plt.title("Sell Analysis")
plt.xlabel("Items")
plt.ylabel("Selling Amount")
plt.legend()

plt.tight_layout()
plt.show()