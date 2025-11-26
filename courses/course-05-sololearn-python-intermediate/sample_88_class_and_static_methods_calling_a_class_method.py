'''
To call a class method you don't need to create an instance of the class. Instead, just use the class name, followed by a dot and the class method name.

Class methods are highly useful for accessing or managing data and functionality that relate to the class itself, rather than to any specific instance.
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

# Using the class method to display information about the series
Book.books_in_series('Harry Potter', 7)