# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_expay = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
num_of_months = 0

while principal > 0:
    num_of_months +=1

    if num_of_months >= extra_payment_start_month and num_of_months <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        num_expay+=1
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

print('Total paid', total_paid,', Number of months', num_of_months)
