'''
Instances share everything that a class has, including the class methods. This means that you call a class method on instances as well.
'''


class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  # Regular method
  def describe_book(self):
    print(f'{self.title} by {self.author}')

  # Class method
  @classmethod
  def books_in_series(cls, series_name, number_of_books):
    print(f'There are {number_of_books} books in the {series_name} series')


# Creating an instance of Book
my_book = Book('Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling')

# Using the instance method to describe the book
my_book.describe_book()

# Calling the class method on the instance
my_book.books_in_series('Harry Potter', 7)