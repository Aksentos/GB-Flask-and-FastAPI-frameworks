"""
Задание №5
� Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте процессы
"""

import multiprocessing
from pathlib import Path


def words_count(filename):
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


if __name__ == "__main__":
    path = Path(Path().cwd() / "texts")
    processes = []

    for obj in path.iterdir():
        if obj.is_file():
            proc = multiprocessing.Process(target=words_count, args=(obj,))
            processes.append(proc)
            proc.start()

    for proc in processes:
        proc.join()
