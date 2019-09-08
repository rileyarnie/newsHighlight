from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
@app.route('/home')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''


    title = 'Home - Welcome to The News Room'

    batman = get_news('batman')
    fifa20 = get_news('fifa20')
    premierLeague = get_news('premierLeague')
    netflix = get_news('netflix')




    return render_template('index.html', batman = batman, fifa20 = fifa20, premierLeague = premierLeague, netflix = netflix)


def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)