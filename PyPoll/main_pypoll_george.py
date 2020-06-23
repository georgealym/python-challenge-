#test
import os
import csv 
import statistics
#open document 
csvpath = os.path.join('..', 'Resources','election_data.csv')
#open and read document as a file 
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #take out the header
    next(csvreader)
    #set voternumber to 0 in preparation to count and set 
    #vote count and candidate to empty in preparation to be list for dictionaries
    voternumber = 0
    votecount = []
    candidate = []
    for row in csvreader: 
        #add the number of rows 
        voternumber +=1   
        #make all the votes their own column with data in the votecount list 
        votecount.append(row[2])
        #find unique candidate names and make them their own list in preparation for the dictionary
        if row[2] not in candidate:
            candidate.append(row[2])
    #set election results as a dictionary
    electionresults_dict={}
    #for each unique candidate in the vote count  
    for candidate in votecount:
        #count  them if you find candidate in vote count and add 1 to the total
        if candidate in electionresults_dict:
            electionresults_dict[candidate] += 1
        #if it isn't on the list, have it maintain its value 
        else:
            electionresults_dict[candidate] = 1 
#identify the winner who has the most votes and only show name by only displaying key 
winner = max(electionresults_dict, key = electionresults_dict.get)
#print results 
print("Election Results")
print("---------------------------------------------------")
print(f'Total Votes: {voternumber}')
print("---------------------------------------------------")
#for each of the dictionary lines, print the candidate key and the value of the total votes and the average percentage 
for key, value in electionresults_dict.items():
    print(f'{key} = {round(value/voternumber*100,3)}% ({value})')
print("---------------------------------------------------")
print(f'Winner: {winner}')
print("---------------------------------------------------")

#create a text file to write to and write results to it
textfile = open ("pypolltextfile.txt","w+")
textfile.write("Election Results")
textfile.write("\n")
textfile.write("---------------------------------------------------")
textfile.write("\n")
textfile.write(f'Total Votes: {voternumber}')
textfile.write("\n")
textfile.write("---------------------------------------------------")
textfile.write("\n")
for key, value in electionresults_dict.items():
    textfile.write(f'{key} = {round(value/voternumber*100,3)}% ({value})')
textfile.write("\n")
textfile.write("---------------------------------------------------")
textfile.write("\n")
textfile.write(f'Winner: {winner}')
textfile.write("\n")
textfile.write("---------------------------------------------------")

textfile.close()