#Import Dependencies
import os
import csv

# Set file path
election_data = os.path.join('PyPoll','Resources','election_data.csv')

#Empty list for looping 
voter_id = []
county = []
candidate = []
runners = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
vote_count = [0,0,0] #each candidate is starting off with 0 votes 

#open csv as read
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ',')

    #Skip over header label
    header = next(csvreader)

    for row in csvreader:
        
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    for runner in candidate:
        if runner == runners[0]:
            vote_count[0]= vote_count[0]+1
        elif runner == runners[1]:
            vote_count[1] = vote_count[1] + 1
        elif runner == runners[2]:
            vote_count[2] = vote_count[2] +1

total_votes = len(voter_id)


voting_percent = []
for count in vote_count:
    percent = round((count / total_votes) * 100, 3)
    voting_percent.append(percent)

winner_index = vote_count.index(max(vote_count))
winner = runners[winner_index]

#Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for x in range(len(runners)): #how many candidates (3)
     print(f"{runners[x]}: {voting_percent[x]}% ({vote_count[x]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


#path for write

election_output = os.path.join('PyPoll', 'Analysis', 'election_data.txt')

with open(election_output, "w") as file:

    file.write('\n')
    file.write('Election Results')
    file.write('\n')
    file.write('----------------------------')
    file.write('\n')
    file.write(f'Total Votes: {total_votes}')
    file.write('\n')
    file.write('----------------------------')
    for x in range(len(runners)):
        file.write('\n')
        file.write(f"{runners[x]}: {voting_percent[x]}% ({vote_count[x]})")
    file.write('\n')
    file.write('----------------------------')
    file.write('\n')
    file.write(f'Winner: {winner}')
    file.write('\n')
    file.write('----------------------------')






