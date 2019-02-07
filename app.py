# import csv

from flask import Flask
from flask import request
import requests
import json

app = Flask(__name__)


@app.route("/")
def index():

    response = requests.get('https://api.etsy.com/v2/listings/active.?api_key=cdwxq4soa7q4zuavbtynj8wx&keywords=bicycle&includes=Images,Shop&sort_on=score')
    data = response.json()

    print(data)

    bicycles = data['results']

    etsy_data = []

    for listing in bicycles:
        etsy_data.append('<li>{}</li>'.format(listing['name'],))

    etsy_data = ''.join(etsy_data)

    # Get html and render to screen
    index_file = open('index.html', 'r')
    index_html = index_file.read()
    index_html = index_html.replace('{{bikes}}', etsy_data)
    index_file.close()

    return index_html
