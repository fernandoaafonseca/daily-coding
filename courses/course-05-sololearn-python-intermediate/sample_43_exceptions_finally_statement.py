'''
You can use the finally statement to perform an operation after the try/except block, no matter if an exception occurred or not.
'''


prices = [559, 879, 'N/A', 349]

try:
  print(sum(prices))
except TypeError:
  print('Check the prices')
finally:
  print('Need help? Contact us')