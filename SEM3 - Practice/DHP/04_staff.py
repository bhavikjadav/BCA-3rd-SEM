"""
Problem: Create Text file and store records in the text file using pipe ( | ) as separator. Tasks:
Create ‘Staff.txt’ file using W+ mode.
Insert five records consists of two attributes ( staff_id and Staff_name) using write() method. Close the file at end.
Open the file in Read (‘r’) mode and read the file using read()method. Display the content of the file using read() method. Close the file.
Open the file in Read (‘r’) mode and read the file using readline()method. Display the content of the file using readline() method. Close the file.
"""

# Writing to a file.
with open('staff.txt', 'w+') as file:
    file.write("101 | Bhavik\n")
    file.write("102 | Sagar\n")
    file.write("103 | Yash\n")
    file.write("104 | Jenish\n")
    file.write("105 | Madhukar\n")
    file.close()

# Reading through read() method.
with open('staff.txt', 'r') as file:
    reader = file.read()
    print(reader)
    file.close()

# Reading through readlines() method.
with open('staff.txt', 'r') as file:
    reader = file.readlines()
    for data in reader:
        print(data)
    file.close()