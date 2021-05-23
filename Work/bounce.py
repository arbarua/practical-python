# bounce.py
#
# Exercise 1.5
height = 100
num_of_bounce = 0
while(num_of_bounce < 10):
    height *= (3/5)
    print(num_of_bounce,' ',round(height,4))
    num_of_bounce+=1
