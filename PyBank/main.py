import os
import csv

#Path to read and write .csv and .txt for PyBank
pybank_csvpath = os.path.join('Resources', 'PyBank_budget_data.csv')
pybank_txtpath = os.path.join('Analysis', 'PyBank_Financial_Records_Analysis.txt')

#PyBank
total_amount = 0
total_changes = 0
increase_profits = None
decrease_profits = None
month_increase_profits = None
month_decrease_profits = None
a = None
count = 0


#PyBank
with open(pybank_csvpath) as pybank_csvfile:
    pybank = dict(csv.reader(pybank_csvfile))

    for months, values in pybank.items():
        
        if values != 'Profit/Losses': #Skip header
            total_amount = total_amount + int(values)
            
            #Determine Greatest Increase in Profits for PyBank
            #Check if it is first row
            if a is None:
                a = int(values) #This variable is used to store the initial value
                continue
            #Assign value to increase_profit at start
            if (increase_profits is None) and (decrease_profits is None):
                #Increase condition
                count = count + 1 
                total_changes = total_changes + (int(values) - a)

                if a < (int(values)): 
                    increase_profits = (int(values) - (a))
                    decrease_profits = 0
                    month_increase_profits = months
                    a = int(values)  #This variable is used here to store previous value for comparison
                #Assign value to decrease_profit at start
                if a > (int(values)):
                    decrease_profits = (int(values) - a)
                    increase_profits = 0
                    month_decrease_profits = months
                    a = int(values)  #This variable is used here to store previous value for comparison               
                continue
            #Equal Profit/Loss values in consecutive months
            if a == (int(values)):
                a = int(values)
                count = count + 1
                continue
            
            #PyBank Increase Profits
            if a < (int(values)):
                total_changes = total_changes + (int(values) - a)
                count = count + 1
                #Substract two values (increase) value' 
                if (int(values) - (a)) >= (increase_profits) :
                    #Decreased value stored
                    increase_profits = (int(values) - a)
                    #Month stored
                    month_increase_profits = months
                #Stored next value for comparison
                a = int(values)
            #PyBank Decrease Profits
            if a > (int(values)):
                total_changes = total_changes + (int(values) - a)
                count = count + 1
                #Substract two change values (decrease) value
                if (int(values) - (a)) <= decrease_profits :
                    #Change value store
                    decrease_profits = (int(values) - a)
                    month_decrease_profits = months
                a = int(values)

#PyBank Format average change value to two decimal places'  
average_change = total_changes/count
average_change = '{:.2f}'.format(average_change)

#Change PyBank date format from 2 digits to 4 digits for the year'    
from datetime import datetime
date_increase = datetime.strptime(month_increase_profits, "%b-%y")
date_decrease = datetime.strptime(month_decrease_profits, "%b-%y")


#Export PyBank Financial Analysis results into a .txt file
with open(pybank_txtpath, 'w') as f:
    f.write('Financial Analysis\n')
    f.write('---------------------------\n')
    f.write('Total Months: ' + str(int(len(pybank))-1) + '\n')
    f.write('Total: ' + '$' + str(total_amount) + '\n')
    f.write('Average Change: ' + '$' + str(average_change) + '\n')
    f.write('Greatest Increase in Profits: ' + str(date_increase.strftime('%b-%Y')) + ' ($' + str(increase_profits) + ')' + '\n')
    f.write('Greatest Decrease in Profits: ' + str(date_decrease.strftime('%b-%Y')) + ' ($' + str(decrease_profits) + ')' + '\n')

#Print PyBank Financial Analysis results to the terminal
print('Financial Analysis')
print('---------------------------')
print('Total Months:', (int(len(pybank))-1))
print('Total:', '$', total_amount)
print('Average Change: ' + '$' + str(average_change)) 
print('Greatest Increase in Profits: ' + str(date_increase.strftime('%b-%Y')) + ' ($' + str(increase_profits) + ')')
print('Greatest Decrease in Profits: ' + str(date_decrease.strftime('%b-%Y')) + ' ($' + str(decrease_profits) + ')' + '\n')