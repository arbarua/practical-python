# pcost.py
#
# Exercise 1.27
import sys
import csv
def portfolio_cost(filename): 
    total_cost = 0
    with open(filename, 'rt') as f:
         rows = csv.reader(f)
         headers = next(rows)
         for line_no,line in enumerate(rows, start = 1):
             record = dict(zip(headers, line))
             try:
                 num_share = int(record['shares'])
                 share_price  = float(record['price'])
             except ValueError:
                 print(f'row no #{line_no}: Contains missing values: [{line}]: replaced with 0s')
                 num_share = 0
                 share_price = 0                     
             total_cost = total_cost+ (num_share * share_price)
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost  = portfolio_cost(filename)
print('Total cost:', cost)

