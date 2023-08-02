"""
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
"""

employee = ["Петр", "Иван"]
rate = [250, 345]
award = ["10.25%", "13.38%"]


def employee_award(names:list, rates: list, bonuses:list):
    """Вычисление бонусов для каждого сотрудника"""
    bonus_dict = {}
    for name, rate, bonus in zip(names, rates, bonuses):
        bonus_percent = float(bonus.strip('%')) / 100
        bonus_dict[name] = rate * bonus_percent
    return bonus_dict


print(employee_award(employee, rate, award))

