import os
import csv


csvpath = os.path.join('Resources', 'budget_data.csv')
#di = dict()
total_amount = 0

average_change = 0
increase_profits = None
decrease_profits = None
month_increase_profits = None
month_decrease_profits = None
a = None
count = 0
#b = None

with open(csvpath) as csvfile:
    #pybank = csv.reader(csvfile, delimiter=',')
    #pybank = csv.DictReader(f, delimiter=',')
    #pybank = list(csv.DictReader(csvfile))
    pybank = dict(csv.reader(csvfile))
    di = {}
    #a = sum ((d['Date']) for d in pybank)
    #print(a)
    for months, values in pybank.items():
        
        #print(values)
        if values != 'Profit/Losses':
            total_amount = total_amount + int(values)
            
            'Determine Greatest Increase in Profits'
            'Check if it is first row'
            if a is None:
                a = int(values)
                continue
            'Assign value to increase_profit at start'
            if (increase_profits is None) and (decrease_profits is None):
                'If second value is either positive/zero or negative'
                ' Increase condition'
                count = count + 1 
                print('None', count)

                if a < (int(values)): 
                    increase_profits = (int(values) - (a))
                    decrease_profits = 0
                    month_increase_profits = months
                    a = int(values)  
                'Assign value to decrease_profit at start'
                if a > (int(values)):
                    decrease_profits = (int(values) - a)
                    increase_profits = 0
                    month_decrease_profits = months
                    a = int(values)                
                continue
            'Equal Profit/Loss values in consecutive months'
            if a == (int(values)):
                a = int(values)
                count = count + 1
                print('Equal', count)
                continue
            
            'Profit increased, first and second value is positive'
            if a < (int(values)):
                count = count + 1
                print('Increase Count', count)
                'Substract two values (increase) value' 
                if (int(values) - (a)) >= (increase_profits) :
                    'Decreased value stored' 
                    increase_profits = (int(values) - (a))
                    'Month stored' 
                    month_increase_profits = months
                    'Stored next value for comparison'                                      
                a = int(values)

            if a > (int(values)):
                count = count + 1
                print('Decrease Count', count)
                'Substract two change values (decrease) value'
                if (int(values) - (a)) <= decrease_profits :
                    'Change value store'
                    decrease_profits = (int(values) - a)
                    month_decrease_profits = months
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


    #month_increase_profitss = datetime.strptime(month_increase_profits, '%m-%Y').date()

    print('Financial Analysis')
    print('----------------------------------')
    print('Total Months:', (int(len(pybank))-1))
    print('Total:', '$', total_amount)
    print('Average Change:', total_amount/(count - 1))) ' Need to update'
    print('Greatest Increase in Profits: ' + month_increase_profits + ' ($' + str(increase_profits) + ')')
    print('Greatest Decrease in Profits: ' + month_decrease_profits + ' ($' + str(decrease_profits) + ')')
    print(count)

