import os
import csv

# Read in the file
csvpath = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip over the header, but save it jic
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        print(row)