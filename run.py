from config import load_config
from flask import Flask
from flask import render_template


app = Flask(__name__)
# app.debug = True
# app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
config = load_config()
app.config.from_object(config)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
