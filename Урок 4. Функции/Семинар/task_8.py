"""
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""

tests = "test value"
variables = "another value"
s = "single letter variable"
check = "this var doesn't end s"


def replace_s_variables():
    variables_dict = globals()
    for var_name in list(variables_dict.keys()):
        if var_name.endswith('s') and var_name != 's':
            new_var_name = var_name[:-1]
            variables_dict[new_var_name] = variables_dict[var_name]
            variables_dict[var_name] = None



print(globals())