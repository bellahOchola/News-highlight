from app import app
import urllib.request,json
from .models import News


api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_BASE_URL"]

# def get_news(category):
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
        news_results: a list of movie objects

    '''
    news_results =[]
    for news in news_list:
        name = news.get('name')
        description = news.get('description')

        news_object = News(name,description)
        news_results.append(news_object)

    return news_results
