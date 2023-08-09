"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию)
"""


def fib_gen(num: int):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


print(list(fib_gen(2)))
