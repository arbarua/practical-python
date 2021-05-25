# report.py
#
# Exercise 2.4
import sys
def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
         headers = next(f).split(',')
         for line in f:
             row = line.split(',')
             holding = (row[0], int(row[1]), float(row[2]))
             portfolio.append(holding)
    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
