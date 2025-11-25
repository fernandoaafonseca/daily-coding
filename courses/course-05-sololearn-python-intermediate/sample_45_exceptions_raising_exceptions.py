'''
You can trigger your own exceptions based on specific conditions using the raise statement. This will immediately stop the program's execution and indicate an error has occurred.

To make the exceptions more helpful for the program users you can add a message describing the error.
'''


print('Rate from 0 to 10')

rate = 15

if rate > 10 or rate < 0:
  raise ValueError('Rate from 0 to 10')