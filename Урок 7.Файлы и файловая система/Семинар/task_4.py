"""
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""
from random import randint


def set_name(min_len, max_len) -> str:
    """Генерация случайного имени в заданном диапазоне"""
    name: str = ''
    for _ in range(randint(min_len, max_len)):
        name += chr(randint(98, 122))
    return name.capitalize()


def create_file(ext: str,
                min_len: int = 6, max_len: int = 30,
                min_size: int = 256, max_size: int = 4096,
                count_files: int = 42):
    """Создание файла"""
    for _ in range(count_files):
        with(open(set_name(min_len, max_len) + ext, "w", encoding='utf-8') as file_output):
            list_of_bytes = bytes([randint(0, 255) for i in range(min_size, max_size)])
            file_output.write(str(list_of_bytes))


if __name__ == '__main__':
    create_file(ext='.txt', count_files=2)















