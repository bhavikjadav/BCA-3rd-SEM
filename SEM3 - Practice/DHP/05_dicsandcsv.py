"""
Use of Dataframe and creating Dataframe from List, Dictionary and CSV file. (Use Pandas library)

Create a list consists of ten names. Use the list to store the list elements in DataFrame. Display the created dataframe.
Create DataFrame from Dictionary which is consists of lists. Create following dictionary consists of three keys and each of them contain corresponding list of values.
d = {
    'Staff':['Meni', 'Krishi', 'Devaan', 'Dhyan'],
    'City':['Pune', 'Delhi', 'Surat', 'Houston'], 
    'Age':[22, 16, 5, 13]
    }
Store above dictionary in dataframe and display the created dataframe.
"""

import pandas as pd

# Create a list consists of ten names. Use the list to store the list elements in DataFrame. Display the created dataframe.
data = ['bhavik', 'sagar', 'madan', 'mathur', 'chitroda', 
        'agnihotr', 'shivaji', 'madhukar', 'chandra', 'muktanand']

df = pd.DataFrame(data)
print(df)

# Create DataFrame from Dictionary which is consists of lists. Create following dictionary consists of three keys and each of them contain corresponding list of values.
d = {
    'Staff':['Meni', 'Krishi', 'Devaan', 'Dhyan'],
    'City':['Pune', 'Delhi', 'Surat', 'Houston'], 
    'Age':[22, 16, 5, 13]
    }

df2 = pd.DataFrame(d)
print(df2)