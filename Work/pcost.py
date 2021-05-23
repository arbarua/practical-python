# pcost.py
#
# Exercise 1.27
total_cost = 0
with open('Data/portfolio.csv', 'rt') as f:
     headers = next(f).split(',')
     for line in f:
         row = line.split()
         for i in range(len(row[0])):
             start = row[0].index(',')+1
             if row[0][i]==',':
                 end = i
         total_cost = total_cost+ (int(row[0][start:end]) * float(row[0][end+1:]))
print("Total cost",total_cost)

