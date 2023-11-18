#!/usr/bin/python3
""" this is the main flask module """
from flask import Flask, render_template
from healthapp.views import user_views


app = Flask(__name__)
app.register_blueprint(user_views)


@app.route('/', strict_slashes=False)
def home():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('notfound.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
