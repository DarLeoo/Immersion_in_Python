"""
Улучшаем задачу 1.
Добавьте возможность запуска функции “угадайки”
из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки
в числовые параметры используйте генераторное выражение.
"""
import random as rnd
from sys import argv

__all__ = ['game']


def game(start: int=1, end: int=4, tries: int=3) -> bool:
    random_num = rnd.randint(start, end)
    for _ in range(tries):
        num_from_user = (int(input("Отгадайте число ")))
        if random_num > num_from_user:
            print("Введенное Вами число меньше загаданного")
        elif random_num < num_from_user:
            print("Введенное Вами число больше загаданного")
        else:
            break
    return random_num == num_from_user


if __name__ == '__main__':
    arguments = map(int, argv[1:])
    print(game(*arguments))

