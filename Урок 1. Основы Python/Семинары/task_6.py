year = int(input("Введите год: "))
LEAP_MAIN = 4
LEAP_EXCLUDE = 100
LEAP_ADDITION = 400

if year % LEAP_MAIN == 0 and year % LEAP_EXCLUDE != 0 or year % LEAP_ADDITION == 0:
    print(year, "- високосный год")
else:
    print(year, "- обычный год")