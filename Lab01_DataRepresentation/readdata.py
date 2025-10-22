# Reading CSV Data s
import csv

FILENAME = 'data.csv'
DATADIR = './Lab01_DataRepresentation/'

with open(DATADIR + FILENAME, 'rt') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(row)

# Each row is a list, Each element within the row is a str, 
# The csv.reader automatically converts all values to strings,regardless of their original format in the CSV file

# Modify programe to deal with the header line separately:
import csv

FILENAME = 'data.csv'
DATADIR = './Lab01_DataRepresentation/'

with open(DATADIR + FILENAME, 'rt') as fp:
    reader = csv.reader(fp)
    header = next(reader)  # Read the header line
    print(f"Header: {header}")
    for row in reader:
        print(row)