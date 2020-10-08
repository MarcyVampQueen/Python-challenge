import os
import csv

# Define outputs
rowCount = 0
totalPL = 0

# Read in the file
csvpath = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip over the header, but save it jic
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        rowCount += 1
        totalPL = totalPL + int(row[1])

print("Financial Analysis\n-------------------------")
print(f"Total Months: {rowCount}")
print(f"Total: ${totalPL}")
# print(f"Average Change: ${}")
# print(f"Greatest Increase in Profits: {} (${})")
# print(f"Greatest Decrease in Profits: {} (${})")