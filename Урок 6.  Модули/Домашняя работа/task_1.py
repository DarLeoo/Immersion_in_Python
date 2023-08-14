from sys import argv



list_28_days = ['02']
list_30_days = ['04', '06', '09', '11']
list_31_days = ['01', '03', '05', '07', '08', '10', '12']


def _leap_year(year: int):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def date_validator(argv:str):
    day, month, year = argv.split('.')
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
    if len(argv) < 2:
        print("Введите дату в формате 'dd.mm.yyyy'")
    else:
        print(date_validator(argv[1]))
