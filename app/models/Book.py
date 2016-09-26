from system.core.model import Model

class Book(Model):
	def __init__(self):
		super(Book, self).__init__()

	def get_books(self):
		query = "SELECT DISTINCT books.title, books.id FROM books JOIN reviews ON books.id = reviews.book_id"
		return self.db.query_db(query)

	def get_book(self, book_id):
		query = "SELECT * from books WHERE id = :id"
		data = { "id": book_id }
		return self.db.query_db(query, data)[0]

	def create_book(self, book, user_id):
		query = "SELECT * from books WHERE title = :title"
		data = { "title": book['title'] }
		book_data = self.db.query_db(query, data)
		if book_data:
			errors = []
			errors.append(("The book is already in the library, please add a new one", "book"))
			return { "status" : False, "errors" : errors}
		query = "INSERT into books (title, author) VALUES(:title, :author)"
		if book['author2']:
			data = {'title': book['title'], 'author': book['author2']}
		else:
			data = {'title': book['title'], 'author': book['author1']}
		book_id = self.db.query_db(query, data)

		query = "INSERT into reviews (content, rating, create_at, user_id, book_id) VALUES(:content, :rating, NOW(), :user_id, :book_id)"
		data = {'content': book['content'], 'rating': book['rating'], 'user_id': user_id, 'book_id': book_id}
		self.db.query_db(query, data)
		return { "status" : True, "book_id" : book_id }

	def get_authors(self):
		query = "SELECT DISTINCT author FROM books"
		return self.db.query_db(query)
