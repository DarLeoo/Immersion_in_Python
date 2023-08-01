"""
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""

my_str = "Напишите функцию, которая принимает строку текста."


def sort_unicode(text):
    return [ord(i) for i in sorted(list(text.replace(" ", '')), reverse=True)]


print(sort_unicode(my_str))


def sort_unicode_second(text):
    return map(ord,
               sorted(list(text.replace(" ", "")),
                      reverse=True))


print(*sort_unicode_second(my_str))

list_2 = []
for i in sorted(list(my_str.replace("", "")), reverse=True):
    list_2.append(ord(i))


print(list_2)