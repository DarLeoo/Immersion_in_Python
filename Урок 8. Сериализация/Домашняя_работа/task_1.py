"""
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории.
 Результаты обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
с учётом всех вложенных файлов и директорий.

Пример:
test/users/names.txt
Результат в json для names.txt:
{
"name": names.txt
"parent": users,
"type": "file"
"size": 4096
"""

import csv
import json
import os
import pickle

__all__ = ['write_info']


def get_info(dir: str, data: list) -> None:
    for i in os.listdir(dir):
        path = dir + '\\' + i
        if os.path.isfile(path):
            data.append({'name': i, 'type': 'file', 'size': os.path.getsize(path),
                         'files': None, 'parent': path.split('\\')[-2]})
        if os.path.isdir(path):
            data.append({'name': i, 'type': 'folder', 'size': None,
                         'files': len(os.listdir(path)), 'parent': None})
            get_info(path, data)


def write_info(dir: str, file_name) -> None:
    data: list = []
    get_info(dir, data)
    create_json(file_name, data)
    create_csv(file_name, data)
    create_pickle(file_name, data)


def create_json(file_name: str, res: list[dict]) -> None:
    with open(f'{file_name}.json', 'w', encoding='UTF-8') as f_wr:
        json.dump(res, f_wr, indent=4)


def create_csv(file_name: str, res: list[dict]) -> None:
    with open(f'{file_name}.csv', 'w', newline='', encoding='UTF-8') as f_wr:
        csv_write = csv.DictWriter(f_wr, fieldnames=['name',
                                                     'type', 'size', 'files', 'parent'])
        csv_write.writeheader()
        csv_write.writerows(res)


def create_pickle(file_name: str, res: list[dict]) -> None:
    with open(f'{file_name}.pickle', 'wb') as f_wr:
        pickle.dump(res, f_wr)


if __name__ == "__main__":
    write_info('C:\\Users\\Лев\\Desktop\\GitHub\\Immersion_in_Python\\Урок 8. Сериализация', 'info_dir')
