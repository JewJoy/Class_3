"""
Две пары
12.04.23
"""

# Про списки можно изучить информацию в Python.md
# https://github.com/JewJoy/Class_3/blob/master/Python.md#%D0%A1%D0%BF%D0%B8%D1%81%D0%BA%D0%B8

var_1 = int(input('Введите значение var_1 - '))

if var_1 > 8:       # если var_1 больше 8
    print('var_1 больше 8')
elif var_1 == 10:   # или же если var_1 равна 10
    print('var_1 равна 10')
elif var_1 < 4:     # или же если var_1 меньше 4
    print('var_1 меньше 4')
else:
    pass    # ничего не делаем

# Использование ТРЕХ двойных кавычек может заменить комментарии в коде (и не только), подробнее расскажу в другой раз
""" 
Ключевое слово pass в Python используется для создания пустого блока кода. Оно может быть использовано в тех местах, 
где синтаксически нужен оператор, но никакого действия не требуется. 

pass не делает ничего и не возвращает никакого значения.
"""

message = input('Введите сообщение - ') # ввод строки (по умолчанию имеет строковой тип (str))
value = int(input('Введите число - '))  # ввод и преобразование строки к типу данных integer (int)


def check(msg: str, val: int):  # функция с именем check, принимает параметры msg типа строки и val типа целого числа
    try:    # конструкция поиска исключений (необязательно)
        if 'Dima' in msg:
            result = val + 10
            return result
        else:
            return None
    except Exception as error:  # если в коде выше была ошибка, то она запишется в переменную 'error'
        print(error)


resp = check(message, value)    # вызов функции
print(resp)     # вывод на экран результата работы функции
print('Вывод после обработки функции')
