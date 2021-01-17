import os
import csv

#Path to read and write .csv and .txt for PyPoll
pypoll_csvpath = os.path.join('Resources', 'PyPoll_election_data.csv')
pypoll_txtpath = os.path.join('Analysis', 'PyPoll_Votes_Analysis.txt')

#PyPoll
pypoll_dict_list = []
candidates_votes = dict()
z = 0

with open(pypoll_csvpath) as pypoll_csvfile:
    pypoll = csv.DictReader(pypoll_csvfile, delimiter = ',')
    
    #Create a list of dictionaries with all the data in the csv file
    for row in pypoll:
        pypoll_dict_list.append(row)
    #Create a dictionary with voting count per candidate
    for x in range(0,len(pypoll_dict_list)):
        candidates_votes[pypoll_dict_list[x]['Candidate']] = candidates_votes.get((pypoll_dict_list[x]['Candidate']), 0) + 1

#Print PyPoll Election Analysis results to the terminal
print('Election Results')
print('-------------------------')
print('Total Votes:', len(pypoll_dict_list))
print('-------------------------')
for candidate, votes in candidates_votes.items(): #Loop to print candidate voting results    
    if votes > z:
        winner = candidate
    z = votes
    percentage = ((votes/(len(pypoll_dict_list)))*100)
    percentage = '{:.3f}'.format(percentage) #Decimal places format
    print(candidate + ':', percentage + '% (' + str(votes) + ')')
    
print('-------------------------')
print('Winner:', winner)
print('-------------------------')

#Export PyPoll Election Analysis results into a .txt file
with open(pypoll_txtpath, 'w') as e:
    e.write('Election Results\n')
    e.write('-------------------------\n')
    e.write('Total Votes: ' + str(len(pypoll_dict_list)) + '\n')
    e.write('-------------------------\n')
    for candidate, votes in candidates_votes.items(): #Loop to print candidate voting results
            percentage = ((votes/(len(pypoll_dict_list)))*100)
            percentage = '{:.3f}'.format(percentage)
            e.writelines([candidate, ': ', percentage, '% (', str(votes), ')\n'])
    e.write('-------------------------\n')
    e.write('Winner: ' + winner + '\n')
    e.write('-------------------------\n')