# main.py

from flask import Flask, render_template, request
from database import getDB, delete, insert

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

    # base_page function returns an HTML template
    # the app.route 'listener'
    return render_template(
        # template file path, starting from folder
        'index.html'
        )


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

        success_entry = insert(isbn, new_book)
        return render_template(
            "index.html", book=new_book, book_was_entered=success_entry
        )

    if request.method == "GET":
        query = request.args.get("search")
        # query may be None, getDB handles
        return render_template("display.html", db=getDB(query), q=query)


@app.route("/api/v1/books", methods=["DELETE"])
def delete_book():
    bid = request.args.get("id")
    print(bid)

    # if bid not passed in URL or undef
    if bid is None or bid == "undefined":
        bid = ""

    if request.method == "DELETE":
        return delete(bid)


@app.route("/search", methods=["GET", "POST"])
def search_page():
    if request.method == "GET":
        return render_template("search.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

# if conditional that runs program
# if the file is being excuted from it's main file source
if __name__ == "__main__":
    # then run the app on 0.0.0.0 on port:5000
    # 127.0.0.1 is localhost on hardware computers
    app.run(debug=True, host="0.0.0.0", port=5000)
