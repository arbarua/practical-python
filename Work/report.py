# report.py
#
# Exercise 2.7 - 2.12
import csv
import fileparse
def print_report(report_name):
    '''prints share names, their prices and change in their prices'''
    #Header added while completing exercise 2.9 and 2.10 so no need to add separately for exercise 2.11
    print(f'{"Name":>10} {"Shares":>10} {"price":>10} {"Change":>10}')#make this comment to produce exercise 2.9
    print("_"*10, "_"*10, "_"*10, "_"*10)#make this comment to produce exercise 2.9
    for r in report_name:
    #print(r) "remove the comment marker from this line to produce exercise 2.9 and remove this statment within double quotation"
        with_dollar = "$"+str(round(r[2],2))# dollar sign added with r[2] = share price
        print(f'{r[0]:>10s} {r[1]:>10d} {with_dollar:>10} {r[3]:>10.2f}')#make this comment to produce exercise 2.9

def calc_portfolio_cost(portfolio_list):
    '''calculates total cost of share in portfolio'''
    calc_total_portfolio_cost = 0.0
    calc_total_portfolio_cost = sum(int(s['shares'])*float(s['price']) for s in portfolio_list)
    print("Total cost:", calc_total_portfolio_cost)
    return calc_total_portfolio_cost

def calc_prices_cost(price_dict, portfolio_list):
    '''calculate the total prices of the shares present in portfolio'''
    calc_total_prices_cost = 0.0
    calc_total_prices_cost = sum(int(s['shares'])*float(price_dict[s['name']]) for s in portfolio_list)
    print("Current value:", calc_total_prices_cost)
    return calc_total_prices_cost

def print_gain_loss(prices_cost, portfolio_cost):
    '''prints if there is gain or loss'''
    if prices_cost > portfolio_cost:
        print(f"Gain: {prices_cost - portfolio_cost:.2f}")
    elif prices_cost < portfolio_cost:
        print(f"Loss: {portfolio_cost - prices_cost:.2f}")
    else:
        print("No Gain, No Loss")

def read_portfolio(filename):
    '''reads porfolio file and make a list with the components in the file'''
    '''portfolio = []
    with open(filename, 'rt') as f:
         rows = csv.reader(f)
         headers = next(rows)
         for line_no, line in enumerate(rows, start = 1):
             record = dict(zip(headers, line))
             portfolio.append(record)'''
    portfolio = fileparse.parse_csv(filename, select = ['name', 'shares', 'price'], types = [str, int, float])         
    return portfolio

def read_prices(filename):
    '''reads file containing the prices of the shares and put the components in a dictionary'''
    '''prices = {}
    f = open(filename, 'r')
    rows = csv.reader(f)
    for line_no,row in enumerate(rows, start = 1):
        if row != []:
             prices[row[0]] = float(row[1])'''
    prices = dict(fileparse.parse_csv(filename, types = [str, float], has_headers = False))
    return prices
    

def make_report(portfolio, prices):
    '''make a report list with name, share cost, share price and changes'''
    report = []
    for s in portfolio:
        report.append((s['name'], int(s['shares']), float(prices[s['name']]), float(prices[s['name']])-float(s['price'])))
    return report

def portfolio_report(portfolio_filename, prices_filename):
    '''calculates portfolio report from files'''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    total_portfolio_cost = calc_portfolio_cost(portfolio)
    total_prices_cost = calc_prices_cost(prices, portfolio)
    #print(total_prices_cost, total_portfolio_cost)
    print_gain_loss(total_prices_cost, total_portfolio_cost)
    report = make_report(portfolio, prices)
    print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

'''#Header added while completing exercise 2.9 and 2.10 so no need to add separately for exercise 2.11
print(f'{"Name":>10} {"Shares":>10} {"price":>10} {"Change":>10}')#make this comment to produce exercise 2.9
print("_"*10, "_"*10, "_"*10, "_"*10)#make this comment to produce exercise 2.9
for r in report:
    #print(r) "remove the comment marker from this line to produce exercise 2.9 and remove this statment within double quotation"
    with_dollar = "$"+str(round(r[2],2))# dollar sign added with r[2] = share price
    print(f'{r[0]:>10s} {r[1]:>10d} {with_dollar:>10} {r[3]:>10.2f}')#make this comment to produce exercise 2.9'''

