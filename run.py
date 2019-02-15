from config import load_config
from flask import Flask
from flask import render_template

app = Flask(__name__)
config = load_config()
app.config.from_object(config)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
