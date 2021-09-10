from os import path
from bs4 import BeautifulSoup
import requests
import csv

CSV = 'myphone.kg.csv'
HOST = 'https://www.myphone.kg/ru'
URL ='https://www.myphone.kg/ru/catalog/cell?sort%5Bby%5D=price_min&sort%5Bord%5D=desc&brn%5B%5D=5&price%5Bmin%5D=&price%5Bmax%5D='
HEADERS = {
    'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'
    'User-Agent:Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
}
def get_html (url, params = ''):
    r =requests.get(url, headers=HEADERS, verify=False, params=params)
    return r    

def get_content (html):
    soup =BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'container')
    news_list = []
    for item in items:
        news_list.append({
            'title': item.find('div', class_ = 'title').get_text(strip=True),
            'price': item.find('div', class_ = 'price').get_text(strip=True),
            'Link': item.find('div', class_ = 'title').find('a').get('href')
        })
        return news_list

def new_save(items, path):
    with open(path, 'a')as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(['Модель Айфона', 'Цена', 'Ссылка'])
        for item in items:
            writer.writerow([item ['title'], item['price'], item['Link']])

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
            print('Цикл завершен')
parce()