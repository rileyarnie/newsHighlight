import unittest
from models import news


news = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News Class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("abc", "def", "this is news", "https://abc.co.ke", "general", "en", "no")


    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))