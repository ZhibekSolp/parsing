
from os import path
from bs4 import BeautifulSoup
import requests
import csv

CSV = 'wildberries_shoe.csv'
HOST = 'https://kg.wildberries.ru/'
URL ='https://kg.wildberries.ru/catalog/obuv/detskaya'
HEADERS = {
    'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8*;q=0.8'
    'User-Agent:Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
}

def get_html (url, params = ''):
    r =requests.get(url, headers=HEADERS, verify=False, params=params)
    return r

def get_content (html):
    soup =BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'product-card__wrapper')
    new_list = []
    for item in items:
        new_list.append({
            'brand_name': item.find('strong', class_ = 'brand-name').find(''),
            'title': item.find('div', class_ = 'product-card__brand-name'),
            'price': item.find('div', class_ ='price'),
            # 'link': item.find('div', class_='product-card__wrapper').find('a').get('href'),
        })
    return new_list

def new_save(items, path):
    with open(path, 'a')as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(['Название бренда', 'Название', 'Цена','Ссылка'])
        for item in items:
            writer.writerow([item ['brand_name'], item ['title'], item['price']])

def parce():
    PEGENATOR = input('Введите количество страниц')
    PEGENATOR = int(PEGENATOR.strip())
    html = get_html(URL)
    if html.status_code == 200:
        news_list = []  
        for page in range(1, PEGENATOR):
            print(f'Страница {page} ГОТОВА')
            html =get_html(URL, params={'page': page})
            news_list.extend(get_content(html.text))
            new_save(news_list, CSV)
            print('ПАРСИНГ ГОТОВ')
        else:
            print('Цикл дошел и вырубился')
parce()