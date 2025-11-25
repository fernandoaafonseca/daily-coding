'''
Vending Machine Selection

Imagine you're programming a vending machine interface. The machine displays a list of products, and the user selects a product by entering its position in the list. To ensure the machine operates smoothly, it should handle cases where users input invalid positions without crashing.

Task
The program below displays a list of products available in a vending machine and asks the user to select a product by entering its index. Complete the program so it either shows the selected product or prints wrong index if the entered index is out of range

Sample Input:
8

Sample Output:
wrong index

In code for this course we always use 2 spaces for indentation.
'''


products = ["Water", "Chocolate", "Chips", "Soda", "Sandwich"]
choice_index = int(input())

# Write a try-except block to display the selected product
try:
  if choice_index in range(len(products)):
    print(products[choice_index])
  else:
    raise ValueError

# or print "wrong index" if the input index is out of range
except ValueError:
  print('wrong index')