import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
#di = dict()
total_amount = 0

average_change = 0
increase_profits = None
decrease_profits = None
month_increase_profits = 0
month_decrease_profits = 0

with open(csvpath) as csvfile:
    #pybank = csv.reader(csvfile, delimiter=',')
    #pybank = csv.DictReader(f, delimiter=',')
    #pybank = list(csv.DictReader(csvfile))
    pybank = dict(csv.reader(csvfile))
    di = {}
    print(type(pybank))
    #next(pybank, None)
    #print(pybank)
    #a = sum ((d['Date']) for d in pybank)
    #print(a)
    for months, values in pybank.items():
        
        #print(values)
        if values != 'Profit/Losses':
            total_amount = total_amount + int(values)
            if increase_profits is None or int(values) > increase_profits:
                increase_profits = int(values)
                month_increase_profits = months
            if decrease_profits is None or int(values) < decrease_profits:
                decrease_profits = int(values)
                month_decrease_profits = months
        

        #total_amount = total_amount + float(values[1])
        #if not months == '':
         #   count = count + 1
        #else:
         #   continue
        #months = months.split(',')[0]
     #   di[months] = di.get(months, 0) + 1
        #print(months[0])
    print('Financial Analysis')
    print('----------------------------------')
    print('Total Months:', (int(len(pybank))-1))
    print('Total:', '$', total_amount)
    print('Average Change:', total_amount/len(pybank))
    print('Greatest Increase in Profits: ' + month_increase_profits + ' ($' + str(increase_profits) + ')')
    print('Greatest Decrease in Profits: ' + month_decrease_profits + ' ($' + str(decrease_profits) + ')')

