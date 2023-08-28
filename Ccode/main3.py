import sys
import ucsv 

# Open the CSV file
with open('C:\\Users\\TusharJagannathPilga\\Desktop\\tushar.csv', 'r') as file:
    # Create a CSV reader
    reader = ucsv.reader(file)

    # Iterate over each row in the CSV file
    for row in reader:
        # Access data in each column
        column1 = row[0]
        column2 = row[1]
        
        # Do something with the data
        print("Column 1:", column1)
        print("Column 2:", column2)
