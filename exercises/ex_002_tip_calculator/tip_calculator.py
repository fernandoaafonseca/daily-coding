print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
tip = float(input('What percentage tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people to split the bill? '))

tip_ammount = bill * tip / 100
total_bill = bill + tip_ammount
bill_per_person = total_bill / people

print(f'Each person should pay: ${bill_per_person}')