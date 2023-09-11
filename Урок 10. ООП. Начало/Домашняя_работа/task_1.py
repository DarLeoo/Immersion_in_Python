"""
Задача 1. Доработаем задания 5-6. Создайте класс-фабрику.
- Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
- Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""

from task_6 import (Dog, Fish, Kotopes)


class Factory:
    def get_animal(self, name_animal: str, *args):
        match name_animal:
            case 'Dog':
                return Dog(*args)
            case 'Fish':
                return Fish(*args)
            case 'Kotopes':
                return Kotopes(args)
        return f'Нет такого животного: {name_animal}'


if __name__ == '__main__':
    animal = Factory()
    dog = animal.get_animal('Dog', 'Буравчик', 2, 'рыжий', 'будьдог', True)
    print(dog)
    animal2 = Factory()
    dog2 = animal.get_animal('Cat', 'Молния', 1, 'белый', 'кот')
    print(dog2)

