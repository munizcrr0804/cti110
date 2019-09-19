#Ramon Muniz
#Calcuate the Sales Prediction
#9/12/19
#CTI-110 P2T1-Sales Prediction
#get the projected sales


total_sales = float(input('Enter the projected sales: '))

# Calcuate the profit as 23 percent of total sales.
profit = total_sales * 0.23


# Dislay the profit
print('The profit is $',format(profit, ',.2f'))
