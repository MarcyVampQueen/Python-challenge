import os
import csv

# Read in the file
csvpath = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")
print(csvpath)
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

# print("Financial Analysis\n-------------------------")
# print(f"Total Months: {}")
# print(f"Total: ${}")
# print(f"Average Change: ${}")
# print(f"Greatest Increase in Profits: {} (${})")
# print(f"Greatest Decrease in Profits: {} (${})")