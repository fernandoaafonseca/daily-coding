'''
Library Management System

Imagine you're developing a library management system. In this system, all items are cataloged as either physical books or ebooks. While both share common attributes like title and author, ebooks also have a file size attribute.

Task
Complete the Ebook class definition by properly initializing it to include the additional file_size attribute. Ensure that instances of Ebook inherit the title and author attributes from the Book class and also add the file_size attribute specific to ebooks.

In code for this course we always use 2 spaces for indentation.
'''


class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author


class Ebook(Book):
  def __init__(self, title, author, file_size):
  # Complete the child class definition
    super().__init__(title, author)
    self.file_size = file_size


my_ebook = Ebook('1984', 'George Orwell', 10)
print(my_ebook.title)
print(my_ebook.author)
print(my_ebook.file_size, 'MB')