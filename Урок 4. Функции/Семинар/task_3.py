"""
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""

my_str = "1 4"


def create_dict(text: str) -> dict[str, int]:
    result = {}
    start, end = sorted(map(int, text.split()))
    for i in range(start, end + 1):
        result[chr(i)] = i
    return result


print(create_dict(my_str))





