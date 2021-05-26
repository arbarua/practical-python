# report.py
#
# Exercise 2.7 - 2.12
import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
         rows = csv.reader(f)
         headers = next(rows)
         for line_no, line in enumerate(rows, start = 1):
             record = dict(zip(headers, line))
             portfolio.append(record)
    return portfolio

def read_prices(filename):
    prices = {}
    f = open('Data/prices.csv', 'r')
    rows = csv.reader(f)
    for line_no,row in enumerate(rows, start = 1):
        if row != []:
             prices[row[0]] = float(row[1])
    return prices

portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')

total_portfolio_cost = 0.0
for s in portfolio:
    total_portfolio_cost += int(s['shares'])*float(s['price'])

print("Total cost:", total_portfolio_cost)

total_prices_cost = 0.0
for s in portfolio:
    total_prices_cost += int(s['shares'])*float(prices[s['name']])

print("Current value:", total_prices_cost)

if total_prices_cost > total_portfolio_cost:
    print(f"Gain: {total_prices_cost - total_portfolio_cost:.2f}")
elif total_prices_cost < total_portfolio_cost:
    print(f"Loss: {total_portfolio_cost - total_prices_cost:.2f}")
else:
    print("No Gain, No Loss")


def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        report.append((s['name'], int(s['shares']), float(prices[s['name']]), float(prices[s['name']])-float(s['price'])))
    return report

report = make_report(portfolio, prices)

#Header added while completing exercise 2.9 and 2.10 so no need to add separately for exercise 2.11
print(f'{"Name":>10} {"Shares":>10} {"price":>10} {"Change":>10}')#make this comment to produce exercise 2.9
print("_"*10, "_"*10, "_"*10, "_"*10)#make this comment to produce exercise 2.9
for r in report:
    #print(r) "remove the comment marker from this line to produce exercise 2.9 and remove this statment within double quotation"
    with_dollar = "$"+str(round(r[2],2))# dollar sign added with r[2] = share price
    print(f'{r[0]:>10s} {r[1]:>10d} {with_dollar:>10} {r[3]:>10.2f}')#make this comment to produce exercise 2.9

