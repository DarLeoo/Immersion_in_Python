"""
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""

companies = {
    'Company_1': [1000, 500, -300, -200],
    'Company_2': [-4000, 400, 434],
    'Company_3': [-100, 13434, 21234]
}


def profit_of_company(dict_values: dict):
    """Функция вычисляет убиточная ли компания, если хотя бы одна да, то возвращает False"""
    all_profitable = True
    result = {}
    for company, profit in dict_values.items():
        total = sum(profit)
        result[company] = total
        if total < 0:
            all_profitable = False
    return result, all_profitable


print(profit_of_company(companies))


def is_profit(comp: dict):
    return all(map(lambda val: sum(val) > 0, comp.values()))


print(is_profit(companies))