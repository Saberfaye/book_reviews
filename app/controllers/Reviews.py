from system.core.controller import *

class Reviews(Controller):
    def __init__(self, action):
        super(Reviews, self).__init__(action)

        self.load_model('Review')
        self.db = self._app.db

    def create(self):
        post = request.form
        self.models["Review"].create_review(post, session["id"])
        return redirect("/books/"+str(post["book_id"]))


    def delete(self, id):
        book_id = self.models["Review"].get_book_id(id)["book_id"]
        self.models["Review"].delete_review(id)
        return redirect("/books/"+str(book_id))



