from unittest import result


'''1) Создайте модуль my_module, в котором будет функция, 
принимающая два аргумента, у которых значения 
по умолчанию должны быть 42 и 12. 
Функция должна возвращать результат их умножения друг на друга. 
Импортируйте функцию в файл main.py, 
вызовите функцию как без аргументов, так и с аргументами. '''

def mult(integer1=42, integer2=12):
    res = integer1*integer2
    return res

