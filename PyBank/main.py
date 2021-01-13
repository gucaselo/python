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
a = None
b = None

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
            
            'Determine Greatest Increase in Profits'
            'Check if it is first row'
            if b is None:
                b = int(values)
                continue
            'Assign value to increase_profit at start'
            if increase_profits is None:
                'If second value is either positive/zero or negative'
                if ((b < (int(values))) and (int(values) >=0)):
                    increase_profits = (int(values) - b)
                    month_increase_profits = months
                    b = int(values)
                    'Both are negative'
                if ((b < int(values)) and (int(values) < 0)):
                    ' Positive output from two negative values' 
                    increase_profits = (int(values) - (b)) 
                    month_increase_profits = months
                    b = int(values)
                'If first value is negative'    


                #continue


            'Profit increased and second value is positive'
            if ((b < (int(values))) and (int(values) >=0)):
                'Substract two change values (decrease) value' 
                if (int(values) - b) > (increase_profits) :
                    'Decreased value stored' 
                    increase_profits = (int(values) - b)
                    'Month stored' 
                    month_increase_profits = months
                    'Stored next value for comparison' 
                    b = int(values)
                    'Profit decreased and second value is negative' 
            if ((b < int(values)) and (int(values) < 0)):
                'Add negative values to account for the change from positive to negative.' 
                if (int(values) - (b))  > increase_profits :
                    'Decreased value stored' 
                    increase_profits = (int(values) - (b))
                    'Month stored' 
                    month_increase_profits = months
                    'stored next value for comparison' 
                    b = int(values) 



            'Determine Greatest Decrease in Profits'
            'Check if it is first row'
            if a is None:
                a = int(values)
                continue
            'Assign value to decrease_profit at start'
            if decrease_profits is None:
                if ((a > (int(values))) and (int(values) >=0)):
                    decrease_profits = (a - int(values))
                    month_decrease_profits = months
                    a = int(values)
                if ((a > int(values)) and (int(values) < 0)):
                    decrease_profits = (int(values) - a)
                    month_decrease_profits = months
                    a = int(values)
                continue

            'Profit decreased and second value is positive'
            if ((a > (int(values))) and (int(values) >=0)):
                'Substract two change values (decrease) value' 
                if (a - int(values)) < (decrease_profits) :
                    'Decreased value stored' 
                    decrease_profits = (a - int(values))
                    'Month stored' 
                    month_decrease_profits = months
                    'Stored next value for comparison' 
                    a = int(values)
                    'Profit decreased and second value is negative' 
            if ((a > int(values)) and (int(values) < 0)):
                'Add negative values to account for the change from positive to negative.' 
                if (int(values) - a)  < decrease_profits :
                    'Decreased value stored' 
                    decrease_profits = (int(values) - a)
                    'Month stored' 
                    month_decrease_profits = months
                    'stored next value for comparison' 
                    a = int(values) 

          #  if ((int(values > a)))
                #increase_profits = int(values)
          #      month_increase_profits = months


        #    if decrease_profits is None or int(values) < decrease_profits:
        #        decrease_profits = int(values)
         #       month_decrease_profits = months
        

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

