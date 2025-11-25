'''
Exceptions are very helpful when your program interacts with user input. While you can't control what a user inputs, you can control your program's behavior when the input doesn't match the expected format. For instance, this program expects a numerical value as input and will throw an exception when the user inputs a non-numerical one.
'''


price = input()

try:
  price_value = int(price)
except ValueError:
  print('Please enter a number')