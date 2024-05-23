"""
Задание №4
� Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте потоки.
"""

import threading
from pathlib import Path


def words_count(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        text = [
            word
            for word in text.replace(".", "").replace("/n", " ").split()
            if word.isalpha()
        ]
        print(f"В файле {filename.stem} количество слов = {len(text)}")


path = Path(Path().cwd() / "texts")
threads = []

for obj in path.iterdir():
    if obj.is_file():
        thread = threading.Thread(target=words_count, args=(obj,))
        threads.append(thread)
        thread.start()

for thread in threads:
    thread.join()
