"""
Задание №1
� Написать программу, которая считывает список из 
10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте потоки.
"""

import threading
import requests
from os import path, getcwd

URLS = [
    "https://www.google.ru/",
    "https://www.ya.ru/",
    "https://www.mail.ru/",
    "https://www.gb.ru/",
    "https://www.animego.org//",
    "https://www.twitch.tv/",
    "https://www.cybersport.ru/",
    "https://www.youtube.com/",
    "https://www.codewars.com/",
    "https://www.vk.com/",
]


def get_data(url: str):
    response = requests.get(url)
    filename = (
        "thred_"
        + url.replace("https://www.", "").replace(".", "_").replace("/", "")
        + ".html"
    )  
    # сохраняем файл в нужную нам папку
    with open(path.join(getcwd(), 'downloads', filename), "w", encoding="utf-8") as file:
        file.write(response.text)


threads = []

for url in URLS:
    tr = threading.Thread(target=get_data, args=(url,))
    threads.append(tr)
    tr.start()

for tr in threads:
    tr.join()
