from app import app
import urllib.request,json
from .models import News,Articles
# import requests


api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_BASE_URL"]
art_url = app.config['ARTICLES_URL']




def get_news(category):
    '''
    function that gets the json response
    '''
    get_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_url) as url:
        get_data = url.read()
        get_response = json.loads(get_data)

        news_results = None

        if get_response['sources']:
            news_list =  get_response['sources']
            news_results = process_sources(news_list)

    return news_results


def process_sources(news_list):
    '''
    function that transforms the results into a list of objects
    
    Args:
        news_list :a list of dictionaries that contain news details

    Returns:
        news_results: a list of news objects

    '''
    news_results =[]
    for news in news_list:
        name = news.get('name')
        id = news.get('id')
        description = news.get('description')

        news_object = News(name,id,description)
        news_results.append(news_object)

    return news_results

def get_articles(id):
    # get_articles_url = art_url.format(source,api_key)
    get_articles_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(id, api_key)
    print(get_articles_url)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)
        articles_results = None

        if  articles_response['articles']:
            articles_list = articles_response['articles']
            articles_results = process_articles(articles_list)

    return articles_results


def process_articles(articles_list):
    articles_results = []

    for article in articles_list:
        id = article.get('id')
        url = article.get('url')
        author = article.get('author')
        description = article.get('description')
        publishedAt = article.get('publishedAt')
        urlToImage = article.get('urlToImage')

        if urlToImage:
            article_object = Articles(id,url,author,description,publishedAt,urlToImage)
            articles_results.append(article_object)
    return articles_results



