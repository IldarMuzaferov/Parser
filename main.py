# способ без генератора(для маленьких сайтов)
import requests
# from bs4 import BeautifulSoup
# from time import sleep
#
# list_card_url = []
#
# headers = {"User-Agent": "Bushizm/22.0 (EVM x8), Drake/1;pd"}
# for count in range(1,8):
#     sleep(3)
#     url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, "lxml")
#     data = soup.find_all('div', class_='w-full rounded border')
#
#     for i in data:
#         card_url = 'https://scrapingclub.com' + i.find('a').get('href')
#         list_card_url.append(card_url)
#
#
# for card_url in list_card_url:
#     response = requests.get(card_url, headers=headers)
#
#     soup = BeautifulSoup(response.text, "lxml")
#
#     data = soup.find('div', class_='my-8 w-full rounded border')
#
#     name = data.find('h3', class_= 'card-title' ).text
#     price = data.find('h4', class_= 'my-4 card-price').text
#     desc = data.find('p', class_= 'card-description').text
#     pic = 'https://scrapingclub.com' + data.find('img').get('src')
#
#     print(name + '\n' + pic + '\n' + price + '\n' + desc)


#СПОСОБ С ГЕНЕРАТОРОМ(ОПТИМИЗИРОВАННЫЙ) И СКАЧИВАНИЕ ИЗОБРАЖЕНИЯ

#Запускаем файл exel_code.py!!!!!!!

import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Bushizm/22.0 (EVM x8), Drake/1;pd"}

#функция для скачивания:
def download(url):
    resp =  requests.get(url, stream=True)
    r = open("D:\\project\\pars\\img" + url.split("/")[-1], 'wb')
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()

def get_url():
    for count in range(1,8):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all('div', class_='w-full rounded border')

        for i in data:
            card_url = 'https://scrapingclub.com' + i.find('a').get('href')
            yield card_url

def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find('div', class_='my-8 w-full rounded border')

        name = data.find('h3', class_= 'card-title' ).text
        price = data.find('h4', class_= 'my-4 card-price').text
        desc = data.find('p', class_= 'card-description').text
        pic = 'https://scrapingclub.com' + data.find('img').get('src')
        download(pic)
        yield name, pic, price, desc
