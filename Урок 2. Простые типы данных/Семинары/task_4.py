"""
    ✔ Напишите программу, которая вычисляет площадь
    круга и длину окружности по введённому диаметру.
    ✔ Диаметр не превышает 1000 у.е.
    ✔ Точность вычислений должна составлять
    не менее 42 знаков после запятой.
"""

from math import pi
import decimal

decimal.getcontext().prec = 44
diam = decimal.Decimal(10)
pi_ = decimal.Decimal(pi)

square = (pi_*diam**2)/4
lenght = pi_ * diam

print((square, lenght))

print(f"всего {str(square).__len__()} знаков")  # проверка общего кол-ва знаков

square_str = str(square)
print(f'{len(square_str.partition(".")[2])} знака после запятой')  # проверка знаков после запятой




