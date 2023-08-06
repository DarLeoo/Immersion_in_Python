"""
Возьмите задачу о банкомате из семинара 2.
 Разбейте её на отдельные операции — функции.
 Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""


start_sum = 0
MINIMUM_AMOUNT = 50
MIN_TAX = 30
MAX_TAX = 600
MAX_BALANCE = 5_000_000
LUXURY_TAX = 0.1
TAX_TAKE = 0.015
BONUS_OPERATION = 0.03
count_of_operation = 0
logs = []

command = {1: 'Пополнить счет', 2: ' Снять деньги со счета', 3: 'Выход'}


def tax_for_luxury(money):
    """Проверка баланса на сумму то, превышается ли сумма в 5кк"""
    if money > MAX_BALANCE:
        balance = (1 - LUXURY_TAX) * money
        return balance
    return money


def sum_of_add_take_validator(cash_sum):
    """Проверка на кратность суммы в 50"""
    if cash_sum > 0 and cash_sum % MINIMUM_AMOUNT == 0:
        return cash_sum
    else:
        print("Внесенная/снятая сумма должна быть больше 0 и кратна 50")


def take_cash(balance, money):
    """Cнятие денег"""
    operation_log("Снятие")
    balance = tax_for_luxury(balance)  # проверка суммы баланса на роскошь
    money = sum_of_add_take_validator(money)
    take_tax_sum = TAX_TAKE * money  # комиссия 1.5%
    if balance > 0 and money < balance:
        if count_of_operation % 2 == 0 and count_of_operation > 0:  # каждая третья операция
            money = (1 + BONUS_OPERATION) * money
        if take_tax_sum < MIN_TAX:
            balance += -MIN_TAX - money
            return balance
        elif take_tax_sum > MAX_TAX:
            balance += - MAX_TAX - money
            return balance
        else:
            balance = take_tax_sum - money
            return balance
    else:
        print("На счету недостаточно средств")


def add_money(balance, money):
    """Внесение денег"""
    operation_log("Внесение")
    balance = tax_for_luxury(balance)
    money = sum_of_add_take_validator(money)
    if count_of_operation % 2 == 0 and count_of_operation > 0:
        money = (1 + BONUS_OPERATION) * money
    return balance + money


def operation_log(act):
    """Добавления лога в список"""
    logs.append(act)
    return logs


while True:
    choice_operation = int(input(""" Выберите желаемое действие:
    1 - Пополнить счет
    2 - Снять деньги со счета
    3 - Выход\n """))
    a = command.get(choice_operation)
    if choice_operation in command:
        if choice_operation == 1:
            cash = int(input("Введите сумму для пополнения\n"))
            start_sum = add_money(start_sum, cash)
            print(f'{start_sum} - баланс после пополнения')
            count_of_operation += 1
        elif choice_operation == 2:
            cash = int(input("Введите сумму для вывода\n"))
            start_sum = take_cash(start_sum, cash)
            print(f'{start_sum} - баланс после снятия')
            count_of_operation += 1
        else:
            print(f'{start_sum} - баланс')
            print(f'{logs} - журнал Ваших действий')
            break
    else:
        print("Некорректное введенное значение")




