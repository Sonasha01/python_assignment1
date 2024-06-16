"""Write a program that reads data from a CSV file and prints it to the 
console. """
import csv

# Specify the file name
filename = 'myfile.csv'

# Open the CSV file
with open(filename, mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Iterate through the rows and print each row
    for row in csv_reader:
        print(row)
