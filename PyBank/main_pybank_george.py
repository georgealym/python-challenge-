#import the dictionary needed in order to do functions 
import os 
import csv 
import statistics
#open document 
csvpath = os.path.join('..', 'Resources','pybank_resources.csv')
#create a list for the total value in preparation for monthly change 
totalvalue = []
#open and read document as a file 
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #take out the header
    next(csvreader)
    #set the number of rows to 0 to add 
    num_rows = 0
    #set monthly change and date value as lists
    monthlychange = []
    months = []
    #take out the first row
    firstrow = next(csvreader)
    #put the first value of the first column in the variable first 
    first = int(firstrow[1])
    #for every row in the table
    for row in csvreader: 
        #add the number of rows 
        num_rows +=1    
        #sum all of the values in that column 
        totalvalue.append(int(row[1]))
        #identify the following variable 
        second = int((row[1]))
        #subtract the following value from the first one in order to get change in new column 
        monthlychange.append(second - first)
        #reset data 
        first = second
        #put all months in a list 
        months.append(row[0])    
    #present number of months, add one because I took out top row 
    numberofmonths = num_rows + 1
    finalnumber = num_rows
    #sum the values from the total volume column 
    total = sum(totalvalue)
    #Average change - take each line and subtract the value from the one below it and divide it by number
    #of rows and round 
    monthlychangetotal = sum(monthlychange)
    average = round(monthlychangetotal/finalnumber,2)
    #minimum monthly change 
    minchange = min(monthlychange)
    #maximum monthly change 
    maxchange = max(monthlychange) 
    print("Financial Analysis")
    print("----------------------------------------------")
    print(f'Total Months: {numberofmonths}')
    print (f'Total: ${total}')
    print (f'Average Change: ${average}')
    #print ("Greatest Increase in Profits: $", datevalue[minchange])
    print ("Greatest Increase in Profits: $", minchange)
    print ("Greatest Decrease in Profits: $", maxchange)
#create a text file to write to and write results to it
textfile = open ("pybanktextfile.txt","w+")
textfile.write("Financial Analysis")
textfile.write("\n")
textfile.write("----------------------------------------------")
textfile.write("\n")
textfile.write(f'Total Months: {numberofmonths}')
textfile.write("\n")
textfile.write (f'Total: ${total}')
textfile.write("\n")
textfile.write (f'Average Change: ${average}')
textfile.write("\n")
textfile.write (f'Greatest Increase in Profits: ($ {minchange})')
textfile.write("\n")
textfile.write (f'Greatest Decrease in Profits: ($ {maxchange})')

textfile.close()