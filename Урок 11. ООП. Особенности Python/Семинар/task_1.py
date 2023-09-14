"""
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
"""
import time


class My_str(str):
    def __new__(cls, value: str, name: str):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.value = value
        instance.time_create = time.time()
        return instance

    def __repr__(self):
        return f'Mystr({self.value=}, {self.name=}, {self.time_create=})'


if __name__ == '__main__':
    str_1 = My_str("Моя строка", name="Лев")
    print(str_1)
    print(repr(str_1))
    print(str_1.name)
    print(str_1.time_create)