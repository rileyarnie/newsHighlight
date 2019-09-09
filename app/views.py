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

