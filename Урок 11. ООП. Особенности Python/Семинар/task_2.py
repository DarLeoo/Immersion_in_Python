"""
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При новом экземпляре класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра
"""


class Archive:
    """Класс,который сохраняет данные из ранее созданных экз."""
    instance = None

    def __new__(cls, *args, **kwargs):
        """Сохранение аргументов в списки"""
        if cls.instance:
            cls.instance.old_text.append(cls.instance.text)
            cls.instance.old_int.append(cls.instance.number)
        else:
            cls.instance = super().__new__(cls)
            cls.instance.old_text = []
            cls.instance.old_int = []
        return cls.instance

    def __init__(self, text: str, number: int) -> None:
        """Конструкт класса с параметрами text, number"""
        self.text = text
        self.number = number

    def __str__(self):
        """Метод строчного выведения экземпляра класса"""
        return f'Текст: {self.text}, Значение: {self.number}'

    def __repr__(self):
        """Метод строчного выведения создания экземпляра класса"""
        return f'Archive({self.text}, {self.number})'


if __name__ == "__main__":
    a1 = Archive(text='T', number=1)
    a2 = Archive(text='E', number=2)
    a3 = Archive(text='Z', number=3)

    print(a2.instance.old_text)
    print(a2.instance.old_int)

    print('---')

    print(a3.text)
    print(a3.number)
    print(a2)