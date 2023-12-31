# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MIN_NUMBER = 0
MAX_NUMBER = 10000


def check_prime(number: int) -> str:
    if number <= MIN_NUMBER or number > MAX_NUMBER:
        return "Введенное число должно быть больше 0 и меньше 100000"
    if number == 1:
        return "Число 1 - не простое число"
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return "Число составное"
    return "Число простое"


number = int(input("Введите число: "))

print(check_prime(number))
