from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
        self.load_model('Review')
        self.db = self._app.db

   
    def index(self):
        return self.load_view('users/index.html')

    def create(self):
        post = request.form
        create_status = self.models["User"].create_user(post)
        if create_status["status"] == False:
            for message in create_status["errors"]:
                flash(message[0], message[1])
            return redirect("/")
        else:
            session["id"] = create_status["user_id"]
            session["alias"] = post["alias"]
            return redirect("/books")

    def login(self):
        post = request.form
        login_status = self.models["User"].login_user(post)
        if login_status["status"] == False:
            for message in login_status["errors"]:
                flash(message[0], message[1])
            return redirect("/")
        else:
            session["id"] = login_status["user_id"]
            session["alias"] = login_status["user_alias"]
            return redirect("/books")

    def show(self, id):
        user = self.models["User"].get_user(id)
        number_reviews = self.models["Review"].get_review_count_of_user(id)["count"]
        books = self.models["User"].get_books_of_review(id)
        return self.load_view('users/show.html', user = user, total_reviews = number_reviews, all_books = books)

    def logout(self):
        session.pop("id")
        session.pop("alias")
        return redirect("/")


