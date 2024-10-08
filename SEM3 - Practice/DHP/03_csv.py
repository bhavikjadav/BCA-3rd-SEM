"""
Write a Python code to create data file (CSV) file using CSV module:

Use open() method of the CSV module to create and open Staff.csv file in “w” mode. The Staff.csv fill will contain (sid, sname, city, age) attributes.
Write a python code to store five records using writerow() method in CSV file. Make sure to add first row containing the title of the attributes.
Write a python code to open the csv file in ‘r’ mode. (Read mode). Using reader() method to display all records available from the data file using for loop.
"""

import csv

# data = {
#     'sid': [101, 102, 103, 104, 105],
#     'sname': ['bhavik', 'rustom', 'amit', 'nitish', 'rimex'],
#     'city': ['surat', 'bhavnagar', 'jamnagar', 'veraval', 'mumbai'],
#     'age': [22, 23, 24, 22, 21]
# }

# Step 1: Create and write to Staff.csv
with open('staff.csv', 'w') as fileobj:
    writer = csv.writer(fileobj)

    # Write Header
    writer.writerow(['sid', 'sname', 'city', 'age'])

    # Writing records
    writer.writerow([101, 'bhavik', 'surat', 22])
    writer.writerow([102, 'ramesh', 'bharuch', 23])
    writer.writerow([103, 'pranav', 'navsari', 24])
    writer.writerow([104, 'kanu', 'bhavnagar', 24])
    writer.writerow([105, 'sandip', 'morbi', 22])

# Step 2: Read from staff.csv
with open('staff.csv', 'r') as file:
    reader = csv.reader(file)

    for data in reader:
        print(data)

