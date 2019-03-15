import os
import csv
import operator

#I did this homework, for both PyBank and PyPoll, in Jupyter Notebook and in python 
# via VS code and terminal--in some cases, iterating between them.  Below i open the 
#data file created in JN that contains the incremental monthly change in profit.

with open('col_output.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    counter = 0
    total = 0
    change = []
    incr = []
    result = {}
    

 # Loop through and establish dictionary of incremental changes in profit/loss.
 # The goal is to extract max/min of change along with the month, making dictionary
 # ideal.

    for row in csvreader:
        #print(row) (allowed me to check the data)
        d = {row[0]:(int(row[2]))}
        result.update(d)
        #print(d) (alllowed me to check the dict)

        date = row[0]
        profitloss = int(row[1])
        change.append(profitloss)
        total += profitloss
        
        # counting months which was verified .unique in JN.

        counter = counter + 1

     # now using a list comprehension to look at increments...another approach.
     # calculating the average change.

    incr = [change[i+1]-change[i] for i in range(len(change)-1)]
    #print(str(incr))
    sumincr = sum(incr)
    avgprofit = sumincr / len(incr)
  
   
    
# creating variables to make report production easier.
 
maxmonth = max(result, key=result.get)
minmonth = min(result, key=result.get)
#print(str(total))
print(" ")
print("Financial Analysis")
print(" ")
print("-------------------------------")
print(" ")
print("Total Months: " + str(counter))
print("Total: $" + str(total))
#print("total of increments is: " + str(sumincr))
print("Average Change: $" + str(round(avgprofit,2)))
print("Greatest Increase in Profits: " + str(maxmonth) + " ($" + str(result[maxmonth]) +")") 
print("Greatest Decrease in Profits: " + str(minmonth) + " ($" + str(result[minmonth]) +")") 
print(" ")


#creating output file

outfile = open('JamesDietzPyBankPythonOutput.txt', 'w')
outfile.write("Financial Analysis\r\n")
outfile.write("-------------------------------\r\n")
outfile.write("Total Months: " + str(counter) + " \r\n")
outfile.write("Total: $" + str(total) + " \r\n")
outfile.write("Average Change: $" + str(round(avgprofit,2)) + " \r\n")
outfile.write("Greatest Increase in Profits: " + str(maxmonth) + " ($" + str(result[maxmonth]) +")\r\n") 
outfile.write("Greatest Decrease in Profits: " + str(minmonth) + " ($" + str(result[minmonth]) +")") 
outfile.close()
