"""Небольшой полуручной скрипт создания однотипных файлов и папок"""
import os
__all__ = ['create_file', 'create_dir']

PLACE = 'C:\\Users\\Лев\\Desktop\\GitHub\\Immersion_in_Python\\'
LIST_NAME = ['Домашняя_работа', 'Семинар']
lesson = input("Тема урока: \n")
numbers_of_task = int(input("Введите кол-во файлов:\n"))
hw_or_sem_choice = int(input("1 - ДЗ, 2 - Семинар:\n"))


def create_dir():
    """Создание директории"""
    if not os.path.exists(f'{PLACE}\\{lesson}'):
        for i in range(2):
            os.makedirs(f'{PLACE}\\{lesson}\\{LIST_NAME[i]}')


def create_file():
    """Создание нужного количество файлов"""
    for j in range(1, numbers_of_task + 1):
        my_file = open(f"{PLACE}\\{lesson}\\{LIST_NAME[hw_or_sem_choice - 1]}\\task_{j}.py", "w+")
        my_file.close()


create_dir(), create_file()
