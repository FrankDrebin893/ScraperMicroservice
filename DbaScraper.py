from flask import Flask
from flask import render_template
from lxml import html
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)


@app.route('/search')
def get_search():
    return render_template("search.html")


@app.route('/scrape')
def get_scrape_result():
    print('Getting scraper result')
    page = requests.get('http://www.dba.dk/soeg/?soeg=gibson+les+paul')

    tree = html.fromstring(page.content)
    #tree = etree.fromstring(page.content)
    #[e.get('.dbaListing') for e in tree.xpath]


    soup = BeautifulSoup(page.content, 'html.parser')
    listingSoup = soup.find_all("tr", { "class" : "dbaListing" })

    print(listingSoup)
    #print(soup.prettify())


    #print(tree)
    return page.text


if __name__ == '__main__':
    app.run()
