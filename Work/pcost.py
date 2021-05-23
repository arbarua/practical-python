# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename): 
    total_cost = 0
    with open(filename, 'rt') as f:
         headers = next(f).split(',')
         for line in f:
             row = line.split()
             for i in range(len(row[0])):
                 start = row[0].index(',')+1
                 if row[0][i]==',':
                     end = i
             total_cost = total_cost+ (int(row[0][start:end]) * float(row[0][end+1:]))
    return total_cost
cost  = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)

