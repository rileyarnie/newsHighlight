import urllib.request, json
from .models import Sources, Articles
from config import Config

import requests

# Sources = news.Sources
# Articles = news.Articles
    # Getting api key
api_key = Config.API_KEY
    # gettting the news base url
base_url = Config.NEWS_API_BASE_URL 
articles_url = Config.NEWS_ARTICLES_API_URL 

def get_sources():
    """
    Function that gets the json response to our url request
    """



    get_sources_url = base_url.format(api_key)

    response = requests.get(get_sources_url)
    source_results_list = response.json()
    # source_results = process_sources(source_results_list)
    # return source_results
    print(source_results_list)

 
    source_result = None

    if source_results_list['sources']:
        source_results = source_results_list['sources']
        results = process_sources(source_results)
    return results


def process_sources(source_results):

    """
    Function  that processes the news result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of movie objects

    """

    source_result = []

    for source_item in source_results:
        id = source_item.get("id")
        name = source_item.get("name")
        description = source_item.get("description")
        url = source_item.get("url")
        category = source_item.get("category")
        language = source_item.get("language")
        country = source_item.get("country")

        source_object = Sources(id, name, description, url, category, language, country)

        source_result.append(source_object)
        print(source_object)
    return source_result

def get_articles(category):
    """
    Function that gets the json response to our url request
    """

    get_articles_url = articles_url.format(category,api_key)
    article_response = requests.get(get_articles_url)
    get_articles_response = article_response.json()
    # source_results = process_sources(source_results_list)
    # return source_results
  

    
    article_result = None 


    if get_articles_response['articles']:
        article_results_list = get_articles_response['articles']
        article_results = process_new_articles(article_results_list)
    return article_results

def process_new_articles(article_results_list):
    """
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain articles details

    Returns :
        articles_results: A list of article objects

    """

    article_result = []

    for article in article_results_list:
        source = article.get("source")
        author = article.get("author")
        description = article.get("description")
        title = article.get("title")
        url = article.get("url")
        urlToImage = article.get("urlToImage")
        publishedAt = article.get("publishedAt")
        
        article_object = Articles(source, author, title, description, url, urlToImage, publishedAt)
        article_result.append(article_object)
    
    return article_result