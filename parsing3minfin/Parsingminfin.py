
# from os import path
# from bs4 import BeautifulSoup
# import requests
# import csv

# CSV = 'minfin.csv'
# HOST = 'http://www.minfin.kg/'
# URL ='http://www.minfin.kg/ru/novosti/mamlekettik-karyz/gosudarstvennyy-dolg'
# HEADERS = {
#     'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8*;q=0.8'
#     'User-Agent:Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
# }

# def get_html (url, params = ''):
#     r =requests.get(url, headers=HEADERS, verify=False, params=params)
#     return r

# def get_content (html):
#     soup =BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_ = 'news')
#     new_list = []
#     for item in items:
#         new_list.append({
#             'data': item.find('div', class_ = 'news_date').get_text(strip=True),
#             'title': item.find('div', class_ = 'news_name').get_text(strip=True),
#             'news': item.find('div', class_ ='news_anons').get_text(strip=True),
#             # 'image': item.find('image', src ='').get_text(strip=True)
#             'link': item.find('div', class_='news_name').find('a').get('href'),
#         })
#     return new_list

# def new_save(items, path):
#     with open(path, 'a')as file:
#         writer = csv.writer(file, delimiter = ';')
#         writer.writerow(['Дата', 'Название', 'Новости','Ссылка'])
#         for item in items:
#             writer.writerow([item ['data'], item ['title'], item['news'],item['link']])

# def parce():
#     PEGENATOR = input('Введите количество страниц')
#     PEGENATOR = int(PEGENATOR.strip())
#     html = get_html(URL)
#     if html.status_code == 200:
#         news_list = []  
#         for page in range(1, PEGENATOR):
#             print(f'Страница {page} ГОТОВА')
#             html =get_html(URL, params={'page': page})
#             news_list.extend(get_content(html.text))
#             new_save(news_list, CSV)
#             print('ПАРСИНГ ГОТОВ')
#         else:
#             print('Цикл дошел и вырубился')
# parce()









import requests
from bs4 import BeautifulSoup


def save():
    with open('moitel.txt', 'a') as file:
        file.writelines(f"Название: {comp['title']}, Цена: {comp['price']}")


def parse():
    URL = 'https://www.myphone.kg/ru/catalog/cell?sort%5Bby%5D=price_min&sort%5Bord%5D=desc&brn%5B%5D=5&price%5Bmin%5D=&price%5Bmax%5D=''https://www.sulpak.kg/f/planshetiy'
    HEADERS = {
        'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'
        'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'

    }

    response = requests.get(URL, headers=HEADERS, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_ ='container')
    comps = []
    print(items)

    for item in items:
        try:
            comps.append({
                'title': item.find('h3', class_ = 'title').get_text(strip=True),
                'price': item.find('div',class_ = 'price' ).get_text(strip=True)
        })
        except:
            pass
    global comp
    for comp in comps:
        print(f"Название: {comp['title']}, Цена: {comp['price']}")
        save()
parse()















# from bs4 import BeautifulSoup
# import requests
# import csv 
# import pandas as pd

# CSV = 'consultant.csv'
# HOST = 'http://www.consultant.ru/'
# URL = 'http://www.consultant.ru/document/cons_doc_LAW_282732/c3345d9a513205fc8b94d810f396d984ac679749/'
# HEADERS = {'User-Agent' :
#   'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' ,
#     'Accept' : 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'}

# def get_html(url, params = ' '):
#     r = requests.get(url, headers = HEADERS, params = params)
#     return r

# def get_content(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('table', class_ = 'dyntable')
#     new_list = []
#     for item in items:
#         new_list.append({
#             'title': item.find('div', class_= 'breakWord').get_text(strip=True), 
            
#         })
#     print(new_list)
#     return new_list


# def new_save(items, path):
#     with open(path, 'a') as file:
#         writer = csv.writer(file, delimiter = ';')
#         writer.writerow(['Дата'])
#         for item in items:
#             writer.writerow([item['title']]) 

# def parse():
#     PAGENATOR = input("Введите количество страниц: ")
#     PAGENATOR = int(PAGENATOR.strip())
#     html = get_html(URL)
#     if html.status_code == 200:
#         new_list = []
#         for page in range(1,PAGENATOR):
#             new_save(new_list, CSV)
#             print('Парсинг готов')
#         else:
#             print("Цикл оконцен")

#             print(f'Страница {page} ГОТОВА!')
#             html = get_html(URL, params={'page':page})
#             new_list.extend(get_content(html.text))



# parse() 