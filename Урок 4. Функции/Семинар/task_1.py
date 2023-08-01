"""
✔ Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
"""

my_text = "Какая-то строка текста! Для преобразования"


def sort_my_unicode(text):
    lst_sorted = sorted(text.split())
    max_word = len(max(lst_sorted, key=len))
    for element, item in enumerate(lst_sorted, start=1):
        print(f"{element} {item:>{max_word}}")


sort_my_unicode(my_text)