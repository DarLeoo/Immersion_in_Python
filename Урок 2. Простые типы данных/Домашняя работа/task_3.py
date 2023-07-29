"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""
from fractions import Fraction


def simplify_fraction(numerator, denominator):
    a, b = numerator, denominator
    while b:
        a, b = b, a % b
    return numerator // a, denominator // a


def add_fractions(fraction1, fraction2):
    num1, den1 = map(int, fraction1.split('/'))
    num2, den2 = map(int, fraction2.split('/'))
    numerator = num1 * den2 + num2 * den1
    denominator = den1 * den2
    return simplify_fraction(numerator, denominator)


def multiply_fractions(fraction1, fraction2):
    num1, den1 = map(int, fraction1.split('/'))
    num2, den2 = map(int, fraction2.split('/'))
    numerator = num1 * num2
    denominator = den1 * den2
    return simplify_fraction(numerator, denominator)


fraction1_str = input("Введите первую дробь в формате a/b: ")
fraction2_str = input("Введите вторую дробь в формате a/b: ")


sum_result = add_fractions(fraction1_str, fraction2_str)
product_result = multiply_fractions(fraction1_str, fraction2_str)
print(f"Сумма дробей: {sum_result[0]}/{sum_result[1]}")
print(f"Произведение дробей: {product_result[0]}/{product_result[1]}")

