'''
Задание №2
� Написать программу, которая считывает список из 
10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте процессы.
'''
import requests # нужно предварительно утсановить
import multiprocessing
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
        "proc_"
        + url.replace("https://www.", "").replace(".", "_").replace("/", "")
        + ".html"
    )
    # сохраняем файл в нужную нам папку
    with open(path.join(getcwd(), 'downloads', filename), "w", encoding="utf-8") as file:
        file.write(response.text)

if __name__ == "__main__":
    processes = []

    for url in URLS:
        proc = multiprocessing.Process(target=get_data, args=(url,))
        processes.append(proc)
        proc.start()

    for proc in processes:
        proc.join()
