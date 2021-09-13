from flask import Flask, render_template, redirect, session, request

from user import User
# import the class from user.py

app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    for user in users:
        print(user)
    return render_template("read(all).html", users = users)


@app.route("/user_signup")
def sign_up_page():
    return render_template('create.html')

@app.route("/create_new", methods=['POST'])
def add_new_user():
    data = { 
    # this 'email' Key in data must be named to match the placeholder in the query.
    "fname": request.form["fname"],
    "lname": request.form["lname"],
    'mail' : request.form['mail'] 
}
    User.create_new(data)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)