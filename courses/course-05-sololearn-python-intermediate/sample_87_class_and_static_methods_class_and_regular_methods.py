'''
Class methods are called on the class itself, not on individual instances. This allows their use without needing to create a class instance. They are especially useful for actions relevant to the class as a whole, rather than actions limited to a single object.

Class methods are created using the @classmethod decorator and take the cls argument, which refers to the class itself.

regular method: self
class method: cls

Here's an example:
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