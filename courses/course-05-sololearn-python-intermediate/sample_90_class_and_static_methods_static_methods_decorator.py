'''
Static methods are similar to class methods, except they don't receive any additional arguments; they are identical to normal functions that belong to a class.

They are marked with the @staticmethod decorator.

When should you use static methods instead of class methods? Static methods don't accept the cls parameter, meaning they can't access or modify the class's state. They are useful when you require functionality that doesn't depend on the class's behavior or instance state and doesn't affect it. Essentially, static methods are suited for tasks that are self-contained and do not require knowledge of the class or instance.
'''


class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  #regular method
  def describe_book(self):
    print(f'{self.title} by {self.author}')

  # Static method
  @staticmethod
  def books_in_series(series_name, number_of_books):
    print(f'There are {number_of_books} books in the {series_name} series')


# Creating an instance of Book
my_book = Book('Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling')

# Using the instance method to describe the book
my_book.describe_book()

# Calling the class method on the instance
my_book.books_in_series('Harry Potter', 7)