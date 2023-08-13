"""
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
"""
from random import randint

__all__ = ['game_guess_two']


def game_guess_two(mystery_num:int, variants: [int], tries: int) -> int:
    for num in range(1, tries + 1):
        rnd_num: int = randint(0, len(variants) - 1)
        if mystery_num == variants[rnd_num]:
            return num
    return 0


if __name__ == '__main__':
    print(game_guess_two(mystery_num=5, variants=[1, 2, 3, 4], tries=10))