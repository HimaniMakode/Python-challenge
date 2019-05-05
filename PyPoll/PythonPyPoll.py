import os
import csv
from collections import Counter
print("Election Results")
print("-----------------------------------------")

csvpath = os.path.join("election_data.csv")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_reader = next(csvreader)
    # initializing variables
    CountVotes = 0
    candidateUniqueName = list()

    for row in csvreader:
        # counting number of months
        CountVotes = CountVotes + 1
        candidateUniqueName.append(row[2])

    vote_counter = Counter(candidateUniqueName)
    # print(vote_counter)

    for candidate_vote in vote_counter:
        percentage_votes = (int(vote_counter[candidate_vote])/int(CountVotes)) * 100
        vote_counter[candidate_vote] = str(round(percentage_votes, 2)) + "% (" + str(vote_counter[candidate_vote])+ ")"

    print("Total votes: " + str(CountVotes))
    print("-----------------------------------------")

    # The percentage of votes each candidate won
    for candidate_vote_percentage in vote_counter:
        print(str(candidate_vote_percentage) + ": " + vote_counter[candidate_vote_percentage])

    # using sorted function, get the 1st value(max) from reverse order of individual vote
    for winner in sorted(vote_counter, key=vote_counter.get, reverse=True)[:1]:
        print("-----------------------------------------")
        print("Winner: " + str(winner))

# output to a text file

    file = open("output_file.txt", "w")
    file.write("Election Results" + "\n")
    file.write("...................................................................................." + "\n")
    file.write("Total votes: " + str(CountVotes) + "\n")
    file.write("...................................................................................." + "\n")
    file.write(str(candidate_vote_percentage) + ": " + vote_counter[candidate_vote_percentage])
    file.write("...................................................................................." + "\n")
    file.write("Winner: " + str(winner))
    file.close()
