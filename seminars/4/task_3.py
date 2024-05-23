"""
Задание №3
� Написать программу, которая считывает список из 
10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте асинхронный подход
"""

import asyncio
import aiohttp  # нужно предварительно утсановить
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


async def get_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            filename = (
                "async_"
                + url.replace("https://www.", "").replace(".", "_").replace("/", "")
                + ".html"
            )
            # сохраняем файл в нужную нам папку
            with open(
                path.join(getcwd(), "downloads", filename), "w", encoding="utf-8"
            ) as file:
                file.write(data)


async def main():
    tasks = []
    for url in URLS:
        task = asyncio.create_task(get_data(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())