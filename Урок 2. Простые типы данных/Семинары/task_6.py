"""
    ✔ Начальная сумма равна нулю
    ✔ Допустимые действия: пополнить, снять, выйти
    ✔ Сумма пополнения и снятия кратны 50 у.е.
    ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
    ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
    ✔ Нельзя снять больше, чем на счёте
    ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
    операцией, даже ошибочной
    ✔ Любое действие выводит сумму денег
"""

start_sum = 0
multiplicity_operation = 50
tax_min = 30
tax_max = 600
tax_withdraw = 0.015
tax_third_operation = 0.03
tax_luxury = 0.1
max_balance = 5_000_000
count_of_operation = 0

command = {1: 'Пополнить счет', 2: ' Снять деньги со счета', 3: 'Выход'}


def tax_for_luxury(cash): # проверка на то, нужно ли брать налог на роскошь или нет
    if cash > max_balance:
        balance = (1 - tax_luxury) * cash # можно было 0.9 сразу кэф поставить, но для гибкости изменения процента добавил переменную
        return balance
    return cash


def sum_of_add_take_validator(cash_sum): # cумма больше 0 и кратна 50
    if cash_sum > 0 and cash_sum % multiplicity_operation == 0:
        return cash_sum
    else:
        print("Внесенная/снятая сумма должна быть больше 0 и кратна 50")


def take_cash(balance, cash):
    balance = tax_for_luxury(balance)  # проверка суммы баланса на роскошь
    cash = sum_of_add_take_validator(cash)
    take_tax_sum = tax_withdraw * cash  # комиссия 1.5%
    if balance > 0 and cash < balance:
        if count_of_operation % 2 == 0 and count_of_operation > 0:  # каждая третья операция
            cash = (1 - tax_third_operation) * cash
        if take_tax_sum < tax_min:
            balance += -tax_min - cash
            return balance
        elif take_tax_sum > tax_max:
            balance += - tax_max - cash
            return balance
        else:
            balance = take_tax_sum - cash
            return balance
    else:
        print("На счету недостаточно средств")


def add_money(balance, cash):
    print(count_of_operation)
    balance = tax_for_luxury(balance)
    cash = sum_of_add_take_validator(cash)
    if count_of_operation % 2 == 0 and count_of_operation > 0:
        cash = (1 - tax_third_operation) * cash
        print(cash)
    print(cash)
    return balance + cash


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
            break
    else:
        print("Некорректное введенное значение")


