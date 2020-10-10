import os
import csv

# Define outputs
totalVotes = 0

# Read in the file
csvpath = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip over the header, but save it jic
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        totalVotes += 1

output = ["Election Results\n-------------------------\n",
     f"Total Votes: {totalVotes}\n-------------------------\n"]
#     f"Total: ${totalProfit_Loss}\n",
#     f"Khan: {}% ({})\n",
#     f"Correy: {}% ({})\n",
#     f"Li: {}% ({})\n",
#     f"O'Tooley: {}% ({})\n",
#     ]

output_path = os.path.join(os.path.dirname(__file__), "analysis", "election_results.txt")

# Open the file and write out each line to it and the terminal
with open(output_path, 'w') as txtfile:
    for line in output:
        #txtfile.write(line)
        print(line, end='')