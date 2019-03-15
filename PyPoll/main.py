import os
import csv
import pandas as pd
import numpy as np

#I did this homework, for both PyBank and PyPoll, in Jupyter Notebook and in python 
# via VS code and terminal--in some cases, iterating between them.  Below i open the 
#data file created in JN that contains dummy variables for each of the candidates.
#it is four columns of data--dichotomous--one for each candidate.


with open('col_output.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
   
   #this allowed me to look at the data in terminal to ensure it was correct.
    #for i,row in enumerate(csvreader):
     #   print(row[0], row[1], row[2], row[3])
    #    if(i >= 9):
     #       break

#   initializing some summation variables

    sumcorrey = 0
    sumkahn = 0
    sumli = 0
    sumotooley = 0
    totalvotes = 0

#   summing votes and storing them.

    for row in csvreader:
        correy = int(row[0])
        kahn = int(row[1])
        li = int(row[2])
        otooley = int(row[3])
        sumcorrey += correy
        sumkahn += kahn
        sumli += li
        sumotooley += otooley

#   calculating total votes cast which is verified in JN and computing percents.

    totalvotes = sumcorrey + sumkahn + sumli + sumotooley
    pctcorrey = sumcorrey / totalvotes * 100
    pctkahn = sumkahn / totalvotes * 100 
    pctli = sumli / totalvotes * 100 
    pctotooley = sumotooley / totalvotes * 100

#   obvious what the outcome is but I created a dictionary to identify max votes which allowed
#   winner determination to be result of code rather than hard coded as string .

    outcome = {"Correy":sumcorrey, "Kahn":sumkahn, "Li":sumli, "O'Tooley":sumotooley}
    winner = max(outcome, key=outcome.get)
    

#again below was done to verify
    #print(sumcorrey)
    #print(sumkahn)
    #print(sumli)
    #print(sumotooley)
    #print(totalvotes)

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
print("Kahn: " + str(round(pctkahn)) + "% (" + str(sumkahn) + ")")
print("Correy: " + str(round(pctcorrey)) + "% (" + str(sumcorrey) + ")")
print("Li: " + str(round(pctli)) + "% (" + str(sumli) + ")")
print("O'Tooley: " + str(round(pctotooley)) + "% (" + str(sumotooley) + ")")
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
outfile.write("Kahn: " + str(round(pctkahn)) + "% (" + str(sumkahn) + ")" + " \r\n")
outfile.write("Correy: " + str(round(pctcorrey)) + "% (" + str(sumcorrey) + ")" + " \r\n")
outfile.write("Li: " + str(round(pctli)) + "% (" + str(sumli) + ")" + " \r\n")
outfile.write("O'Tooley: " + str(round(pctotooley)) + "% (" + str(sumotooley) + ")" + " \r\n")
outfile.write("________________________________\r\n")
outfile.write("Winner: " + str(winner) + " with " + str(outcome[winner]) + " votes." + " \r\n")
outfile.write("_________________________________")
outfile.close()
