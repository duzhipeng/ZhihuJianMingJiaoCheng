from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.debug = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


# 搜索电影
class SearchForm(FlaskForm):
    keywords = StringField('电影关键词', validators=[DataRequired('电影关键词不能为空。')])
    submit = SubmitField('搜索')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        keywords = form.keywords.data
        payload = {'q': keywords}
        r = requests.get('https://api.douban.com/v2/movie/search', params=payload)
        data = r.json()['subjects']
        return render_template('return.html', form=form, data=data)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
