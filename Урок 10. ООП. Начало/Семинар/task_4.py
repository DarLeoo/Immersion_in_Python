"""
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""
import random


def sum_digit(a:int):
    a =  str(a)
    sum_a = 0
    for i in a:
        sum_a += int(i)
    return sum_a % 7


class Person:
    def __init__(self, surname, name, patronymic, age):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.__age = age

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} {self.__age}'


class Employ(Person):
    def __init__(self, surname, name, patronymic, age):
        super().__init__(surname, name, patronymic, age)
        self.id = random.randint(100_000, 999_999)
        self.level = sum_digit(self.id)


if __name__ == '__main__':
    p1 = Employ('Ivanov', 'Ivan', 'Ivanovich', 25)
    print(p1)
    print(p1.get_age())
    print(p1.id, p1.level)