from flask import render_template
from app import app
from .request import get_news,get_articles


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    general_news = get_news('general')
    return render_template('index.html', general = general_news)

# @app.route('/articles/<id>')
# def articles(id):
#     '''
#     returns the articles page and its data
#     '''
#     news_articles = get_articles(id)
#     id = id
#     print(news_articles)
#     return render_template('articles.html',artiq = news_articles, id = id)
