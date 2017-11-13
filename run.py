from flask import Flask
from flask import render_template, request, redirect, url_for
import requests

app = Flask(__name__)
app.debug = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
