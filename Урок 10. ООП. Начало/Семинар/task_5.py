"""
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""
class Dog:
    def __init__(self, name:str, age: int,  color: str, breed: str, is_domestic: bool = True) -> None:
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed
        self.is_domestic = is_domestic

    def __str__(self):
        if self.is_domestic:
            return f'Собака {self.color} {self.breed} домашняя'
        return f'Собака {self.color} {self.breed} дворняга'


class Kotopes:
    def __init__(self, age: int, name: str, number_heads: int = 2) -> None:
        self.age = age
        self.name = name
        self.__number_heads = number_heads

    def __str__(self):
        return f'Kotopes -> number_heads: {self.__number_heads} '


class Fish():
    def __init__(self, name, age, aqua, size):
        self.name = name
        self.age = age
        self.aqua = aqua
        self.size = size

    def __str__(self):
        if self.aqua:
            return f'{self.name} морская'
        else:
            return f'{self.name} пресноводная'


if __name__ == '__main__':
    dog = Dog('Роки', 3, 'черный', 'мопс', True)
    dog2 = Dog('Барсик', 5, 'рыжий', 'французский бульдог', False)
    print(dog,'|',dog2)
    print(Kotopes(age=11, name='Miracle', number_heads=2))