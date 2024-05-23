"""
Задание №6
� Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте асинхронный подход.
"""

import asyncio
from pathlib import Path


async def words_count(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        text = [
            word
            for word in text.replace(".", "")
            .replace(",", "")
            .replace("/n", " ")
            .split()
            if word.isalpha()
        ]
        print(f"В файле {filename.stem} количество слов = {len(text)}")


async def main():
    path = Path(Path().cwd() / "texts")
    tasks = [asyncio.ensure_future(words_count(obj)) for obj in path.iterdir() if obj.is_file()]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
