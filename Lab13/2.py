# 
#
# Keane Kouchi
# 11/6/24

from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app instance
app = Flask(__name__)

USERS = {
    "port": "port123",
    "kazman": "kazman123"
}

# Route for the home page (index)
@app.route("/")

# a. Create an index.html page that allows a user to select a link that takes them to a login page.
def index():
    return render_template("index.html")

# b. Create a login.html page--a simple form with a text field for a username, a password field for a password,
#  and a submit button. Create a route for /login. The function for login should present the form.
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Check if the username and password match
        if USERS.get(username) == password:
            return redirect(url_for("success", username=username))
        else:
            return "Invalid credentials, please try again."
        

    return render_template("login.html")

# c. When this form is submitted, process the data and take the user to a success page. 
# You can hard-code a dictionary of userids and passwords such as:
#USERS = {"port": "port123", "kazman": "kazman123"}
@app.route("/success/<username>")
def success(username):
    return render_template("success.html", username=username)

# Run the application in debug mode
if __name__ == "__main__":
    app.run(debug=True)

