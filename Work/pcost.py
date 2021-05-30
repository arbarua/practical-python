# pcost.py
#
# Exercise 1.27
import sys
import report
def portfolio_cost(filename): 
    total_cost = 0           
    for record in report.read_portfolio(filename):
          try:
                 num_share = int(record['shares'])
                 share_price  = float(record['price'])
          except ValueError:
                 print(f'row no #{line_no}: Contains missing values: [{line}]: replaced with 0s')
                 num_share = 0
                 share_price = 0
          total_cost = total_cost+ (num_share * share_price)
    return total_cost

def main():
    if len(sys.argv)!=2:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile')
    cost = portfolio_cost(sys.argv[1])
    print('Total cost:', cost)

if __name__ == '__main__':
    main()
'''if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost  = portfolio_cost(filename)
print('Total cost:', cost)'''


