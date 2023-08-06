"""
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
используйте его строковое представление.
Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}
"""


def is_hash(val_key) -> bool:
    try:
        hash(val_key)
        return True
    except TypeError:
        return False


def create_dict(**kwargs) -> dict:
    reversed_dict = {}
    for key, value in kwargs.items():
        if is_hash(value) is True:
            reversed_dict[value] = key
        else:
            reversed_dict[str(value)] = key
    return reversed_dict


print(create_dict(res=1, reverse=[1, 2, 3]))




