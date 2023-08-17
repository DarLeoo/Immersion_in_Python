"""
Напишите функцию группового переименования файлов. Она должна:
- принимать параметр желаемое конечное имя файлов. При переименовании
 в конце имени добавляется порядковый номер.
- принимать параметр количество цифр в порядковом номере.
- принимать параметр расширение исходного файла. Переименование должно работать
только для этих файлов внутри каталога.
- принимать параметр расширение конечного файла.
- принимать диапазон сохраняемого оригинального имени. Например, для диапазона [3, 6]
 берутся буквы с 3 по 6 из
исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
 Далее счётчик файлов и расширение.

Пример:
rename(wanted_name = "video", count_nums=3,
 extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
foto_2002.txt -> o_20video001.csv
"""
from pathlib import Path

__all__ = ['rename_file']


def _get_old_name(old_name: str, span: list[int]) -> str:
    """Получение текущего имени"""
    if len(old_name) < span[0]:
        res = ''
    elif len(old_name) <= span[1]:
        res = old_name[span[0] - 1:]
    else:
        res = old_name[span[0] - 1:span[1]]
    return res


def rename_file(wanted_name: str = "video", count_nums: int = 3,
                extension_old: str = ".txt", extension_new: str = ".csv",
                span: list[int] = [3, 6]):
    """Переименование файлов"""
    number = 1
    p = Path(Path().cwd())
    for file in p.iterdir():
        full_name = str(file).split('\\')[-1]
        ext = full_name.split('.')[1]
        print(ext, extension_old)
        if ext == extension_old:
            old_name = _get_old_name(full_name.split('.')[0], span)
            serial_number = (('0' * (count_nums - len(str(number)))
                               + str(number)))
            number += 1
            Path(full_name).rename(f'{old_name}{wanted_name}{serial_number}.{extension_new}')


if __name__ == '__main__':
    rename_file(wanted_name='video', count_nums=3,
                extension_old='txt', extension_new='doc',
                span=[3, 6])
