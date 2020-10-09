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
        totalProfit_Loss += int(row[1])
        newPL = int(row[1])

        # We don't care about the P/L change the first time
        if rowCount == 1:
            oldPL = newPL
        PL_change = newPL - oldPL
        PL_avgChange = PL_avgChange + PL_change

        # Check for greatest
        if PL_change > greatest["Increase"]:
            greatest["Increase"] = PL_change
            greatest["IncMonth"] = row[0]
        elif PL_change < greatest["Decrease"]:
            greatest["Decrease"] = PL_change
            greatest["DecMonth"] = row[0]

        oldPL = newPL

output = ["Financial Analysis\n-------------------------\n",
    f"Total Months: {rowCount}\n",
    f"Total: ${totalProfit_Loss}\n",
    f"Average Change: ${PL_avgChange/(rowCount-1)}\n",
    f"Greatest Increase in Profits: {greatest['IncMonth']} (${greatest['Increase']})\n",
    f"Greatest Decrease in Profits: {greatest['DecMonth']} (${greatest['Decrease']})"
    ]

output_path = os.path.join(os.path.dirname(__file__), "analysis", "budget_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    for line in output:
        txtfile.write(line)
        print(line, end='')