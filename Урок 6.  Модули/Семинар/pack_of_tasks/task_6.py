"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""
__all__ = ['date_validator']


date = '29.02.2004'
list_28_days = ['02']
list_30_days = ['04', '06', '09', '11']
list_31_days = ['01', '03', '05', '07', '08', '10', '12']


def _leap_year(year: int):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def date_validator(date: str):
    day, month, year = date.split('.')
    if month in list_31_days and 0 < int(day) < 32 and 0 < int(year) < 10_000:
        return True
    elif month in list_30_days and 0 < int(day) < 31 and 0 < int(year) < 10_000:
        return True
    elif month in list_28_days and 0 < int(day) < 30 and 0 < int(year) < 10_000 and _leap_year(int(year)):
        return True
    elif month in list_31_days and 0 < int(day) < 32 and 0 < int(year) < 10_000 and not _leap_year(int(year)):
        return True
    return False


if __name__ == '__main__':
    print(date_validator(date))
