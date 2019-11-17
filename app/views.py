from flask import render_template
from app import app
from .request import get_news


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    general_news = get_news('general')
    return render_template('index.html', general = general_news)
