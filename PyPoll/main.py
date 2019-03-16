# James Dietz
# HW 3
# Data Analytics and Visulation, 3

import os
import csv



with open('election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    correy = 0
    khan = 0
    li = 0
    otooley = 0
    
    
# counting votes. I would have liked to have come up with a way to not have
# to hard code candidates names but I couldnt figure out how to determine
#unique values of candidate column and use that to count
    for row in csvreader:
     
        vote = row[2]
        if vote == "Correy":
            correy = correy + 1
        elif vote == "Khan":
            khan = khan + 1
        elif vote == "Li":
            li = li + 1
        elif vote == "O'Tooley":
            otooley = otooley + 1

# percentage and total votes calcs
    totalvotes = correy + khan + li + otooley
    pctcorrey = correy / totalvotes * 100
    pctkhan = khan / totalvotes * 100 
    pctli = li / totalvotes * 100 
    pctotooley = otooley / totalvotes * 100

#below was done to verify
#print(str(correy))
#print(str(khan))
#print(str(li))
#print(str(otooley))

#   obvious what the outcome is but I created a dictionary to identify max votes which allowed
#   winner determination to be result of code rather than hard coded as string .
outcome = {"Correy":correy, "Kahn":khan, "Li":li, "O'Tooley":otooley}
winner = max(outcome, key=outcome.get)


# reporting code
   
print(" ")
print('')
print("Election Results")
print(" ")
print("_______________________________")
print(" ")
print("Total Votes: " + str(totalvotes))
print(" ")
print("________________________________")
print("Khan: " + str(round(pctkhan)) + "% (" + str(khan) + ")")
print("Correy: " + str(round(pctcorrey)) + "% (" + str(correy) + ")")
print("Li: " + str(round(pctli)) + "% (" + str(li) + ")")
print("O'Tooley: " + str(round(pctotooley)) + "% (" + str(otooley) + ")")
print("________________________________")
print("Winner: " + str(winner) + " with " + str(outcome[winner]) + " votes.")
print("_________________________________")
print (" ")

# code to produce text file as called for in instructions.

outfile = open('JamesDietzPyPollPythonOutput.txt', 'w')
outfile.write("Election Results\r\n")
outfile.write("-------------------------------\r\n")
outfile.write("Total Votes: " + str(totalvotes) + " \r\n")
outfile.write("-------------------------------\r\n")   
outfile.write("Khan: " + str(round(pctkhan)) + "% (" + str(khan) + ")" + " \r\n")
outfile.write("Correy: " + str(round(pctcorrey)) + "% (" + str(correy) + ")" + " \r\n")
outfile.write("Li: " + str(round(pctli)) + "% (" + str(li) + ")" + " \r\n")
outfile.write("O'Tooley: " + str(round(pctotooley)) + "% (" + str(otooley) + ")" + " \r\n")
outfile.write("________________________________\r\n")
outfile.write("Winner: " + str(winner) + " with " + str(outcome[winner]) + " votes." + " \r\n")
outfile.write("_________________________________")
outfile.close()

        