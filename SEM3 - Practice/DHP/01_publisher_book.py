"""Create the following table and solve the question based on this.

PUBLISHER(PUBLISHER_NAME,CITY,COUNTRY,CONTACTNO,DATE_FOUNDED)
BOOK(BOOKNO,BOOKNAME,PUBLISHED_YEAR,PAGES,PUBLISHER_NAME)

Create trigger for publisher that it should not allow country name other than ""UK"" and contactno should be 11 digit and first digit should be 0.

Create a trigger on book table where it should not allowed books which has pages less than 100 and published year should not greater than current year.

Export the data of book and publisher table to Mydata.csv file

Export the stucture  of book and publisher table to structure.txt file

Import the book stock detail from book_stock.csv file to book_stock table.columns of book_stock.csv files are bookno , bookname, no of book sale, availabe qty of book """

# Perform this using SQLITE