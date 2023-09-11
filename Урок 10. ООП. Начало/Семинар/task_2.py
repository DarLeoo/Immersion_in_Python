"""
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:
    def __init__(self, length: float, width: float = None):
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    def calc_len(self):
        return (self.width + self.length) * 2

    def calc_area(self):
        return self.width + self.length


if __name__ == '__main__':
    r_1 = Rectangle(length=2, width=5)
    print(r_1.calc_len())
    print(r_1.calc_area())

    print('----')

    r_2 = Rectangle(length=2)
    print(r_2.calc_area())
    print(r_2.calc_len())