"""
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""
from random import randint, choice


EXTEN = ['.txt', '.doc', '.pdf']


def set_name(min_len, max_len) -> str:
    """Генерация случайного имени в заданном диапазоне"""
    name: str = ''
    for _ in range(randint(min_len, max_len)):
        name += chr(randint(98, 122))
    return name.capitalize()


def create_file(ext: str,
                min_len: int = 6, max_len: int = 30,
                min_size: int = 256, max_size: int = 4096,
                count_files: int = 5):
    """Создание файла"""
    for _ in range(count_files):
        with(open(set_name(min_len, max_len) + ext, "w", encoding='utf-8') as file_output):
            list_of_bytes = bytes([randint(0, 255) for i in range(min_size, max_size)])
            file_output.write(str(list_of_bytes))


def create_ext():
    """Выбор расширения файла"""
    create_file(ext=choice(EXTEN))


if __name__ == '__main__':
    create_ext()