"""
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""


def sort_num(num_list: list):
    for i in range(len(num_list)):
        for j in range(i, len(num_list)):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    return num_list


num_list = [1, 3, 4, 11, 10, 9]


print(sort_num(num_list))