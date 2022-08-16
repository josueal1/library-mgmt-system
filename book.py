# book.py

'''Class definition of the Book objection'''

class Book():
	def __init__(self, title: str, author: str, isbn_10: str):
		self.title = title
		self.author = author
		self.isbn_10 = isbn_10
