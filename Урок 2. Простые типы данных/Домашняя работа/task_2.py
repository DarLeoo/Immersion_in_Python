"""
  Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
  Функцию hex используйте для проверки своего результата.
"""


num = 88

hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
hex_string = ''

print(hex(num))
while num > 0:
    remainder = num % 16
    if remainder >= 10:
        hex_string = hex_dict[remainder] + hex_string
    else:
        hex_string = str(remainder) + hex_string
    num //= 16

print(f"Шестнадцатеричное представление числа: {hex_string}")
