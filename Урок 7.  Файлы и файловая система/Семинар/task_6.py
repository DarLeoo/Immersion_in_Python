"""
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
from os import getcwd, listdir,mkdir
from random import randint, choice


def set_name(min_len, max_len) -> str:
    """Генерация случайного имени в заданном диапазоне"""
    name: str = ''
    for _ in range(randint(min_len, max_len)):
        name += chr(randint(98, 122))
    return name.capitalize()


def create_files(ext: str, directory: str = '', min_len: int = 6,
                 max_len: int = 30, min_size: int = 256,
                 max_size: int = 4096, count_files: int = 42):
    """Создание файла"""
    if not directory:
        directory = getcwd() + '\\'
    else:
        if directory not in listdir():
            mkdir(directory)
        directory = getcwd() + '\\' + directory + '\\'
    for _ in range(count_files):
        with open(directory + set_name(min_len, max_len) + ext, 'w',
                  encoding='utf-8') as output:
            list_of_bytes = bytes([randint(0, 255) for x in range(min_size,
                                                                  max_size)])
            output.write(str(list_of_bytes))


if __name__ == "__main__":
    EXTINSIONS = ['.pdf', '.csv', '.txt', '.doc']
    create_files(ext=choice(EXTINSIONS), directory='test_dir', count_files=58)