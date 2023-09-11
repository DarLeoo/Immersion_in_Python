"""
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""

import math


class Circle:
    _pi = math.pi

    def __init__(self, radius):
        self.radius = radius

    def calc_len(self):
        return self._pi * self.radius * 2

    def calc_area(self):
        return self._pi * self.radius ** 2


print(Circle.calc_len(Circle(23)))
print(Circle.calc_area(Circle(23)))