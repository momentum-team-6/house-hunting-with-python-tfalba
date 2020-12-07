# These are given at start
current_savings = 0
r = .04
portion_down_payment = .25

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

count = 0
while current_savings < total_cost*portion_down_payment:
  count += 1
  current_savings += (current_savings*r)/12 + portion_saved*(annual_salary/12)

print('Number of months: ' + str(count))
