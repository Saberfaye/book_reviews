from system.core.model import Model

class Review(Model):
	def __init__(self):
		super(Review, self).__init__()

	def get_all_reviews(self):
		query = "SELECT books.title, books.id AS book_id, reviews.rating, users.alias, users.id AS user_id, reviews.content, reviews.create_at FROM users JOIN reviews ON users.id = reviews.user_id JOIN books ON books.id = reviews.book_id ORDER BY reviews.create_at DESC LIMIT 3"
		return self.db.query_db(query)

	def get_reviews_of_book(self, book_id):
		query = "SELECT reviews.rating, users.alias, users.id AS user_id, reviews.id, reviews.content, reviews.create_at, reviews.book_id FROM users JOIN reviews ON users.id = reviews.user_id WHERE reviews.book_id = :book_id ORDER BY reviews.create_at ASC"
		data = { "book_id" : book_id}
		return self.db.query_db(query, data)

	def get_review_count_of_user(self, user_id):
		query = "SELECT COUNT(user_id) AS count FROM reviews WHERE user_id = :user_id"
		data = { "user_id" : user_id }
		return self.db.query_db(query, data)[0]

	def create_review(self, review, user_id):
		query = "INSERT into reviews (content, rating, create_at, user_id, book_id) VALUES(:content, :rating, NOW(), :user_id, :book_id)"
		data = {'content': review['content'], 'rating': review['rating'], 'user_id': user_id, 'book_id': review['book_id']}
		return self.db.query_db(query, data)

	def delete_review(self, review_id):
		query = "DELETE FROM reviews WHERE id = :id"
		data = { "id" : review_id}
		return self.db.query_db(query, data)

	def get_book_id(self, review_id):
		query = "SELECT book_id FROM reviews WHERE id = :id"
		data = { "id" : review_id}
		return self.db.query_db(query, data)[0]
