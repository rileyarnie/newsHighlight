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
            news_results = process_results(news_results_list)
    return news_results

    def process_results(news_list):

        '''
        Function  that processes the news result and transform them to a list of Objects

        Args:
            news_list: A list of dictionaries that contain news details

        Returns :
            news_results: A list of movie objects

        '''

        news_results = []
        for news_item in news_list:
            id = news_item.get("id")
            name = news_item.get("name")
            description = news_item.get("description")
            url = news_item.get("url")
            category = news_item.get("category")
            language = news_item.get("language")
            country = news_item.get("country")

            news_object = News(id,name,description,url,category,language,country)

            news_results.append(news_object)

        return news_results





