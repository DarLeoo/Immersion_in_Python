MIN_NUMBER = 1
MAX_NUMBER = 999
message = ""

num = int(input("Введите число от 1 до 999: \n"))
if MIN_NUMBER <= MAX_NUMBER <= 999:
    if num < 10:
        result = num ** 2
        message = "Введена цифра, возвращён её квадрат: " + str(result)
    elif num < 100:
        first_digit = num // 10
        second_digit = num % 10
        result = first_digit * second_digit
        message = "Введено двузначное число, возвращено произведение цифр: " + str(result)
    else:
        revers_num = int(str(num)[::-1])
        message = "Введено трехзначное число, возвращено зеркальное число: " + str(revers_num)
else:
    message = "Введено некорректное значение, введите число от 1 до 999"

print(message)



