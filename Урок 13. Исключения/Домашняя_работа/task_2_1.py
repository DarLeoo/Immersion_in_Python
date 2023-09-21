"""
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""
from task_2 import RadiusError
import math


class Circle:
    _pi = math.pi

    def __init__(self, radius) -> None:
        self.validate_radius(radius)
        self.radius = radius

    def calc_len(self):
        return self._pi * self.radius * 2

    def validate_radius(self, radius):
        if radius < 0:
            raise RadiusError

    def calc_area(self):
        return self._pi * self.radius ** 2


if __name__ == '__main__':
    c1 = Circle(-1)




