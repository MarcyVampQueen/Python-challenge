import os
import csv

# Define outputs
rowCount = 0
totalProfit_Loss = 0
PL_avgChange = 0
oldPL = 0
greatest = {"Increase":0,"IncMonth": "", "Decrease":0,"DecMonth":""}

# Read in the file
csvpath = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip over the header, but save it jic
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        rowCount += 1
        totalProfit_Loss = totalProfit_Loss + int(row[1])
        newPL = int(row[1])
        PL_change = newPL - oldPL
        PL_avgChange = PL_avgChange + PL_change
        oldPL = int(row[1])
        if PL_change > greatest["Increase"]:
            greatest["Increase"] = PL_change
            greatest["IncMonth"] = row[0]
        elif PL_change < greatest["Decrease"]:
            greatest["Decrease"] = PL_change
            greatest["DecMonth"] = row[0]

print("Financial Analysis\n-------------------------")
print(f"Total Months: {rowCount}")
print(f"Total: ${totalProfit_Loss}")
print(f"Average Change: ${PL_change/(rowCount)}")
print(f"Greatest Increase in Profits: {greatest['IncMonth']} (${greatest['Increase']})")
print(f"Greatest Decrease in Profits: {greatest['DecMonth']} (${greatest['Decrease']})")