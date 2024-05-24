"""
Задание №7
� Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами
от 1 до 100.
� При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
� В каждом решении нужно вывести время выполнения
вычислений.
"""

import time
from random import randint
import threading
import multiprocessing
import asyncio


def summ_arr():
    arr = [randint(1, 100) for _ in range(1_000_000)]
    result = sum(arr)
    print(f"Сумма = {result}, Время выполнения: {time.time()-start:.2f} секунд")


# """
# Многопоточный подход
# """

start = time.time()
threads = []

for _ in range(5):
    thr = threading.Thread(target=summ_arr)
    threads.append(thr)
    thr.start()

for thr in threads:
    thr.join()

print(f"Общее время работы при многопоточном подходе: {time.time()-start:.2f} секунд")


"""
Многопроцессорный подход
"""

start = time.time()
processes = []

if __name__ == "__main__":
    for _ in range(5):
        proc = multiprocessing.Process(target=summ_arr)
        processes.append(proc)
        proc.start()

    for proc in processes:
        proc.join()

    print(
        f"Общее время работы при многопроцессорном подходе: {time.time()-start:.2f} секунд"
    )


"""
Асинхронный подход
"""


async def summ_arrgs():
    arr = [randint(1, 100) for _ in range(1_000_000)]
    result = sum(arr)
    print(f"Сумма = {result}, Время выполнения: {time.time()-start:.2f} секунд")


async def main():
    tasks = [asyncio.create_task(summ_arrgs()) for _ in range(5)]
    await asyncio.gather(*tasks)


start = time.time()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(f"Общее время работы при асинхронном подходе: {time.time()-start:.2f} секунд")
