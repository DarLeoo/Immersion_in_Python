"""
Задача 2. Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства.
Задания должны решаться через вызов методов экземпляра.Задача
"""

"""
Возьмите задачу о банкомате из семинара 2.
 Разбейте её на отдельные операции — функции.
 Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.min_amount = 50
        self.min_tax = 30
        self.max_tax = 600
        self.max_balance = 5_000_000
        self.luxury_tax = 0.1
        self.tax_take = 0.015
        self.bonus_operation = 0.03
        self.count_of_operation = 0
        self.logs = []

    def tax_for_luxury(self, money):
        """Проверка баланса на сумму то, превышается ли сумма в 5кк"""
        if money > self.max_balance:
            balance = (1 - self.luxury_tax) * money
            return balance
        return money

    def sum_of_add_take_validator(self, cash_sum):
        """Проверка на кратность суммы в 50"""
        if cash_sum > 0 and cash_sum % self.min_amount == 0:
            return cash_sum
        else:
            print("Внесенная/снятая сумма должна быть больше 0 и кратна 50")

    def take_cash(self, money):
        """Снятие денег"""
        self.operation_log("Снятие")
        self.balance = self.tax_for_luxury(self.balance)  # проверка суммы баланса на роскошь
        money = self.sum_of_add_take_validator(money)
        take_tax_sum = self.tax_take * money  # комиссия 1.5%
        if self.balance > 0 and money < self.balance:
            if self.count_of_operation % 2 == 0 and self.count_of_operation > 0:  # каждая третья операция
                money = (1 + self.bonus_operation) * money
            if take_tax_sum < self.min_tax:
                self.balance += -self.min_tax - money
                return self.balance
            elif take_tax_sum > self.max_tax:
                self.balance += -self.max_tax - money
                return self.balance
            else:
                self.balance = take_tax_sum - money
                return self.balance
        else:
            print("На счету недостаточно средств")

    def add_money(self, money):
        """Внесение денег"""
        self.operation_log("Внесение")
        self.balance = self.tax_for_luxury(self.balance)
        money = self.sum_of_add_take_validator(money)
        if self.count_of_operation % 2 == 0 and self.count_of_operation > 0:
            money = (1 + self.bonus_operation) * money
        self.balance += money

    def operation_log(self, act):
        """Добавления лога в список"""
        self.logs.append(act)

    def display_balance(self):
        """Отображение баланса и журнала действий"""
        print(f'{self.balance} - баланс')
        print(f'{self.logs} - журнал Ваших действий')


bank_account = BankAccount()

while True:
    choice_operation = int(input("""Выберите желаемое действие:
    1 - Пополнить счет
    2 - Снять деньги со счета
    3 - Выход\n"""))

    if choice_operation == 1:
        cash = int(input("Введите сумму для пополнения\n"))
        bank_account.add_money(cash)
        print(f'{bank_account.balance} - баланс после пополнения')
        bank_account.count_of_operation += 1
    elif choice_operation == 2:
        cash = int(input("Введите сумму для вывода\n"))
        bank_account.take_cash(cash)
        print(f'{bank_account.balance} - баланс после снятия')
        bank_account.count_of_operation += 1
    elif choice_operation == 3:
        bank_account.display_balance()
        break
    else:
        print("Некорректное введенное значение")








