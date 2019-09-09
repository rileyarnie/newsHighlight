from flask import render_template
from app import app
from .request import get_sources, get_articles

# Views
@app.route('/sources')

def index():
    
    '''
    View root page function that returns the index page and its data
    '''



    batman_news = get_sources()

    title = 'Home|Welcome to The News Room'



    return render_template('sources.html', batman = batman_news)

@app.route('/articles')
def showArticles():

    '''
    View news page function that returns the news articles page and its data
    '''

    tech_news = get_articles('technology')

    climate_news = get_articles('climate')

    us_politics = get_articles ('uspolitics')

    
    sports_news = get_articles('sports')
   

    return render_template('articles.html', technology = tech_news, climate = climate_news, uspolitics = us_politics ,sports = sports_news)


@app.route('/trending')
def trending_articles():
    
    '''
    View news page function that returns the trending news articles page and its data
    '''

    
    trending_news = get_articles('trending')
   

    return render_template('trending.html', trending = trending_news)

@app.route('/')
def home_articles():
    
    '''
    View news page function that returns the trending news articles page and its data
    '''
    batsy_news = get_articles('batman')
    dc_news = get_articles('dccomics')
    marvel_news = get_articles('marvel')
    africa_news = get_articles('africa')
   

    return render_template('index.html', batman = batsy_news, dccomics = dc_news, marvel = marvel_news, africa = africa_news)