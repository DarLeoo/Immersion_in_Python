"""
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
"""
from random import randint
from typing import List, Dict

__all__ = ['game_guess_two', 'all_var']


def game_guess_two(mystery_num:int, variants: List[int], tries: int) -> int:
    for num in range(1, tries + 1):
        rnd_num: int = randint(0, len(variants) - 1)
        if mystery_num == variants[rnd_num]:
            return num
    return 0


VAR_DICT: Dict = {1: [1, 2, 3, 4], 2: [2, 3, 4, 5]}


def all_var():
    for key, value in VAR_DICT.items():
        print(game_guess_two(mystery_num=key, variants=value, tries=10))


if __name__ == '__main__':
    all_var()