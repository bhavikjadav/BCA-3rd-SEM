"""
"Sales (sid, year, totalsales)
Create above table into a SQLite database with appropriate constraints.
Insert at least 10 records into the sales table.
Export sales table data into sales.csv file.
Write a python scripts that read the sales.csv file and plot a line chart that shows totalsales of the year. Also decorate the chart with appropriate title, lables, colours etc."
"""

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('new_sales.db')
cursor = conn.cursor()

# Task 1: Create above table into a SQLite database with appropriate constraints
# cursor.execute('''
#     CREATE TABLE NEW_SALES(
#         SID INTEGER PRIMARY KEY,
#         YEAR INTEGER,
#         TOTAL_SALES REAL           
#     );
# ''')

# Task 2: Insert at least 10 records into the sales table
# data = [
#     (1, 2020, 15000.45),
#     (2, 2021, 12000.45),
#     (3, 2022, 10000.45),
#     (4, 2023, 9000.45),
#     (5, 2024, 5500.45),
#     (6, 2020, 6000.45),
#     (7, 2021, 25000.45),
#     (8, 2022, 14500.45),
#     (9, 2023, 22000.45),
#     (10, 2024, 13255.45)
# ]

# cursor.executemany("INSERT INTO NEW_SALES (SID, YEAR, TOTAL_SALES) values (?, ?, ?)", data)

# conn.commit()
# conn.close()

df = pd.read_sql_query('SELECT * FROM NEW_SALES;', conn)
print(df)

# # Task 3: Export sales table data into sales.csv file
df.to_csv('sales.csv')

# # Task 4: Plotting
plt.plot(df['YEAR'], df['TOTAL_SALES'])
plt.xlabel("Year")
plt.ylabel("Total_Sales")
plt.title("Sales Analysis")
plt.legend()
plt.show()