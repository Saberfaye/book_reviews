from system.core.controller import *

class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)

        self.load_model('Book')
        self.load_model('Review')
        self.db = self._app.db

   
    def index(self):
        reviews = self.models["Review"].get_all_reviews()
        books_with_reviews = self.models["Book"].get_books()
        return self.load_view('books/index.html', all_reviews = reviews, all_books_with_reviews = books_with_reviews)

    def add(self):
        authors = self.models["Book"].get_authors()
        return self.load_view('books/add.html', all_authors = authors)

    def create(self):
        post = request.form
        created_status = self.models["Book"].create_book(post, session["id"])
        if created_status["status"] == True:
            return redirect("/books/"+str(created_status["book_id"]))
        else:
            for message in created_status["errors"]:
                flash(message[0], message[1])
            return redirect("/books/add")

    def show(self, id):
        book = self.models["Book"].get_book(id)
        reviews = self.models["Review"].get_reviews_of_book(id)
        return self.load_view('books/show.html', book = book, all_reviews = reviews)


