# Install Flask and create a first simple application.
#
# Keane Kouchi
# 11/6/24

from flask import Flask, render_template, request, redirect, url_for

# a. Run Flask in debug mode. This means you will access your local server at 127.0.0.1
app = Flask(__name__)

# b. Create a single route for “/”.
@app.route("/")

# c. Respond to a request for this route by outputting “Welcome to a very boring web site!”
def index():
    return "Welcome to a very boring web site!"

if __name__ == "__main__":
    app.run(debug=True)
