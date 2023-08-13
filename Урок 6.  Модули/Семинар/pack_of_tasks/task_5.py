"""
Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
и число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания
из защищённого словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.
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
_res: Dict = {}


def all_var():
    for key, value in VAR_DICT.items():
        _res[str(value)] = game_guess_two(mystery_num=key, variants=value, tries=10)
        print(_res[str(value)])


if __name__ == '__main__':
    all_var()
    print(_res)