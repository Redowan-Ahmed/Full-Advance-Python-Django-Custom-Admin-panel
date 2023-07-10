from bs4 import BeautifulSoup
import requests
from .models import ScrapedProduct


def get_all_products_data():
    try:
        page = requests.get('https://www.aliexpress.com/category/7/computer-office.html')
        soup = BeautifulSoup(page.content, features='html.parser')
        data = soup.find_all('a', class_ = 'manhattan--container--1lP57Ag cards--gallery--2o6yJVt search-card-item')
        for product in data:
            anchoretag = product.get('href')
            
            for h1 in product.findAll('h1'):
                text = h1.text
                return ScrapedProduct.objects.get_or_create(title = text, url = anchoretag)
    except Exception as e:
        print(f"Error occurred while getting all products data. Error message is {e}")
        
""" 
def get_all_products_by_url_data(slug):
    try:
        data = str(slug).split('-')
        actualdata = '/'.join(data)
        page = requests.get(f'https://www.aliexpress.com/{actualdata}.html')
        soup = BeautifulSoup(page.content, features='html.parser')
        data = soup.find_all('a', class_ = 'manhattan--container--1lP57Ag cards--gallery--2o6yJVt search-card-item')
        for product in data:
            anchoretag = product.get('href')

            for h1 in product.findAll('h1'):
                text = h1.text
                return ScrapedProduct.objects.get_or_create(title = text, url = anchoretag)
    except Exception as e:
        print(f"Error occurred while getting all products data. Error message is {e}") """