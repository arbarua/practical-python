# report.py
#
# Exercise 2.7
import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
         headers = next(f).split(',')
         for line in f:
             row = line.split(',')
             holding = {'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])}
             portfolio.append(holding)
    return portfolio

def read_prices(filename):
    prices = {}
    f = open('Data/prices.csv', 'r')
    rows = csv.reader(f)
    for row in rows:
         if row != []:
             prices[row[0]] = float(row[1])
    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_portfolio_cost = 0.0
for s in portfolio:
    total_portfolio_cost += s['shares']*s['price']

print("Total cost:", total_portfolio_cost)

total_prices_cost = 0.0
for s in portfolio:
    total_prices_cost += s['shares']*prices[s['name']]

print("Current value:", total_prices_cost)

if total_prices_cost > total_portfolio_cost:
    print(f"Gain: {total_prices_cost - total_portfolio_cost:.2f}")
elif total_prices_cost < total_portfolio_cost:
    print(f"Loss: {total_portfolio_cost - total_prices_cost:.2f}")
else:
    print("No Gain, No Loss")
