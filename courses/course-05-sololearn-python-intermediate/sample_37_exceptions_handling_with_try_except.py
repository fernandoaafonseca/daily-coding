'''
Exceptions often arise from a variety of causes, including invalid input, out-of-bounds indices, incompatible type operations, and logical errors in the code. The good news is that exceptions are often predictable, allowing developers to anticipate and handle them effectively.

In this lesson, you will learn how to handle exceptions and prevent your program from failing during execution.

Exceptions can often be predictable. To handle them and prevent program failure, you can use a try/except statement.

The try block holds code that might cause an exception. If an exception occurs, execution of the try block stops, and the except block is executed, allowing the program to continue running.
'''


prices = [250, 300, '240', 400]

try:
  # Block that may cause an exception
  total = sum(prices)
  print(total)

except TypeError:
  # To perform if there is an exception
  print('Invalid data type')

print('Happy Shopping')