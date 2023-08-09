"""
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


def split_path_info(path: str):
    *absolut, file = path.split('/')
    return '/'.join(absolut), *file.split('.')


print(split_path_info("C:/Users/Lev/Desktop/test.txt"))