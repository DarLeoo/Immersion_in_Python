"""
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции
"""
from random import randint, uniform


def create_file(name_file: str, count_line: int) -> None:
    """Создание файла"""
    name_file += '.txt'
    with open(name_file, 'a', encoding='utf=8') as f:
        for _ in range(count_line + 1):
            f.write(f'{randint(-1000, 1000)} | {uniform(-1000, 1000)}\n')


if __name__ == '__main__':
    create_file(name_file="numbers",
                count_line=5)
