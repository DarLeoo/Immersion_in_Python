"""
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
"""


def read_and_write(numbers_file: str,
                   names_file: str,
                   output_file: str) -> None:
    """Чтение и запись в новом файле"""
    with(open(numbers_file, 'r', encoding='utf-8') as file_numbers,
         open(names_file, 'r', encoding='utf-8') as file_names):
        names = file_names.read().split('\n')
        numbers = file_numbers.read().split('\n')
    if len(numbers) > len(names):
        names += names[:len(numbers)-len(names)]
    else:
        numbers += numbers[:len(names) - len(numbers)]

    with open(output_file, 'w', encoding='utf-8') as file_output:
        for name, number in zip(names, numbers):
            if not name or not number:
                break
            number_output_int, number_output_float = map(float, number.split(' | '))
            multiplication = number_output_int * number_output_float
            if multiplication < 0:
                file_output.write(f'{name.lower()} {abs(multiplication)} \n')
            else:
                file_output.write(f'{name.upper()} {int(multiplication)} \n')


if __name__ == '__main__':
    read_and_write('numbers.txt', 'names.txt', 'result')

