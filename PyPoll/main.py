import os
import csv

# Define outputs
totalVotes = 0
oldWin = 0
winner = ""
candidates = {}

# Read in the file
csvpath = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip over the header, but save it jic
    csv_header = next(csvreader)

    # Read each row of data and count
    for row in csvreader:
        totalVotes += 1

        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

output = ["Election Results\n-------------------------\n", f"Total Votes: {totalVotes}\n-------------------------\n"]
for name, votes in candidates.items():
    percentWin = votes/totalVotes
    output.append(f"{name}: {'{0:.2%}'.format(percentWin)} ({votes})\n")
    if percentWin > oldWin:
        winner = name
    oldWin = percentWin
output.append(f"-------------------------\nWinner: {winner}\n-------------------------")

output_path = os.path.join(os.path.dirname(__file__), "analysis", "election_results.txt")

# Open the file and write out each line to it and the terminal
with open(output_path, 'w') as txtfile:
    for line in output:
        txtfile.write(line)
        print(line, end='')