from flask import Flask
from flask import render_template
from lxml import html
import requests


app = Flask(__name__)


@app.route('/search')
def get_search():
    return render_template("search.html")


@app.route('/scrape')
def get_scrape_result():
    print('Getting scraper result')
    page = requests.get('http://dba.dk')
    tree = html.fromstring(page.content)
    print(tree)
    return page.text


if __name__ == '__main__':
    app.run()
