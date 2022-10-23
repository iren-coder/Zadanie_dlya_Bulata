'''Напишите функцию, которая принимает число n и генерирует словарь, 
чьи ключи состоят из чисел от 1 до n, а их значения -- куб ключей. 
Пример: передано число 5. В результате должны получить словарь 
{1: 1, 2: 8, 3: 27, 4: 64}'''

def cube(n):
    my_dict = {i : i ** 3 for i in range(1, n)}
    return my_dict

print(cube(5))
# >>> {1: 1, 2: 8, 3: 27, 4: 64}

print(cube(9))
# >>> {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512}
