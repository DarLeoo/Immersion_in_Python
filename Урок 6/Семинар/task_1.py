"""
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""
import random as rnd


def game(start: int, end: int, tries: int) -> bool:
    random_num = rnd.randint(start, end)
    for _ in range(tries):
        num_from_user = (int(input("Отгадайте число ")))
        if random_num > num_from_user:
            print("Введенное Вами число меньше загаданного")
        elif random_num < num_from_user:
            print("Введенное Вами число больше загаданного")
        else:
            break
    return random_num == num_from_user


if __name__ == '__main__':
    print(game(1, 4, 3))