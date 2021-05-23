# pcost.py
#
# Exercise 1.27
import sys
def portfolio_cost(filename): 
    total_cost = 0
    with open(filename, 'rt') as f:
         headers = next(f).split(',')
         for line in f:
             row = line.split(',')
             try:
                 num_share = int(row[1])
                 share_price  = float(row[2])
             except ValueError:
                 print("some fields were missing, replaced with 0")
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

