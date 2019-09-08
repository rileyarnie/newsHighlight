from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

#gettting the news base url

base_url = app.config['NEWS_API_BASE_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''

    news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(news_url) as url:
        news_data = url.read()
        news_response = json.loads(news_data)

        news_results = None

        if news_response['results']:
            news_results_list = news_response['results']
            news_results = process__results(news_results_list)
    return news_results


