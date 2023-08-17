"""
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
from random import randint
__all__ = ['create_file', 'set_name']


def set_name() -> str:
    """Генерация различных имён"""
    name: str = ''
    for _ in range(randint(4, 7)):
        name += chr(randint(98, 122))
    return name.capitalize()


def create_file(name_file: str, count_line: int) -> None:
    """Создание файла с именами"""
    name_file += '.txt'
    with open(name_file, 'a', encoding='utf=8') as f:
        for _ in range(count_line + 1):
            f.write(f'{set_name()}\n')


if __name__ == '__main__':
    create_file(name_file='names',
                count_line=5)
