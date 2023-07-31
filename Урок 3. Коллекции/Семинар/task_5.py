"""
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
"""

nums_list = [1, 2, 3, 4, 4, 2, 5, 6, 7, 8]
new_nums_list = []
for i, elem in enumerate(nums_list, start=1):
    if elem % 2 != 0:
        new_nums_list.append(i)

print(new_nums_list)