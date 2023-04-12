"""
Две пары
12.04.23
"""

# Про списки можно изучить информацию в Python.md
# https://github.com/JewJoy/Class_3/blob/master/Python.md#%D0%A1%D0%BF%D0%B8%D1%81%D0%BA%D0%B8

var_1 = int(input('Введите значение var_1 - '))

if var_1 > 8:
    print('var_1 больше 8')
elif var_1 == 10:
    print('var_1 равна 10')
elif var_1 < 4:
    print('var_1 меньше 4')
else:
    pass    # ничего не делаем

# Использование ТРЕХ двойных кавычек может заменить комментарии в коде (и не только), подробнее расскажу в другой раз
""" 
Ключевое слово pass в Python используется для создания пустого блока кода. Оно может быть использовано в тех местах, 
где синтаксически нужен оператор, но никакого действия не требуется. 

pass не делает ничего и не возвращает никакого значения.
"""

message = input('Введите сообщение - ')
value = int(input('Введите число - '))


def check(msg: str, val: int):
    try:
        if 'Dima' in msg:
            result = val + 10
            return result
        else:
            return None
    except Exception as error:
        print(error)


resp = check(message, value)    # вызов функции
print(resp)     # вывод на экран результата работы функции
print('Вывод после обработки функции')