# importting python "libraries"
# other code we can reuse "frameworks"
from flask import Flask, render_template, request
from database import getDB, delete, insert
import random

# Create a flask app
app = Flask(
    # pass down name of py file implicitly
    __name__,
    # Name of html file folder
    template_folder='templates',
    # Name of directory for static files
    static_folder='static')


# What happens when the user visits the site
# We'll serve an HTML page mgmt system
@app.route('/')
@app.route('/insert')
def base_page():
    # Sets the random number
    random_num = random.randint(1, 100000)

    # base_page function returns an HTML template
    # the app.route 'listener'
    return render_template(
        # template file path, starting from folder
        'insert.html',
        # Sets the var random_number in the template
        random_number=random_num)


@app.route("/books", methods=["GET", "POST"])
# book_page function handles the HTTPs requests
def book_page():
    if request.method == "POST":
        # grabbing info given from the submitted HTML form
        isbn = request.form["isbn"]
        title = request.form["title"]
        author = request.form["author"]
        edition = request.form["edition"]
        publication = request.form["publication"]

        new_book = {
            "isbn": isbn,
            "title": title,
            "author": author,
            "edition": edition,
            "publication": publication
        }

        insert(isbn, new_book)

        return render_template(
            "base.html", book=new_book, book_was_entered=True)

    if request.method == "GET":
        query = request.args.get("search")
        # query may be None, getDB handles
        return render_template("display.html", db=getDB(query))


@app.route("/api/v1/books", methods=["DELETE"])
def delete_book():
    bid = request.args.get("id")
    if bid is None:
        bid = ""

    if request.method == "DELETE":
        return delete(bid)


@app.route("/search", methods=["GET", "POST"])
def search_page():
    if request.method == "GET":
        return render_template("search.html")


# if conditional that runs program
# if the file is being excuted from it's main file source
if __name__ == "__main__":
    # then run the app on 0.0.0.0 on port:5000
    # 127.0.0.1 is localhost on hardware computers
    app.run(debug=True, host="0.0.0.0", port=5000)
