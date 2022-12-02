"""
Задать натуральное число k.
Сформируйте многочлен (полином) степени k со случайными коэффициентами из промежутка от 0 до 100, включительно.
Многочлен вывести в консоль и записать в файл.

Ввод: значение типа <int>
Вывод: значение типа <str>, файл с одной строкой.

Пример:
2
2x^2 + 4x + 5 = 0
"""

from random import randint

max_value = 100
k = int(input('Введите коэффициент: '))


def get_rand(num):
    mult = [randint(0, max_value) for i in range(num)] + [randint(1, max_value)]
    return mult


def get_poly(num, multi):
    polynom = ' + '.join([f'{(j, "")[j == 1]}x^{i}' for i, j in enumerate(multi) if j][::-1])
    polynom = polynom.replace('x^1+', 'x+')
    polynom = polynom.replace('x^0', '')
    polynom += ('', '1')[polynom[-1] == '+']
    polynom = (polynom, polynom[:-2])[polynom[-2:] == '^1']
    return polynom


multiple = get_rand(k)
polynom1 = get_poly(k, multiple)
print(polynom1)

with open('task3.txt', 'w') as data:
    data.write(polynom1)

# Многочлен для следующей задачи:

k = int(input('Введите коэффициент: '))

multiple = get_rand(k)
polynom2 = get_poly(k, multiple)
print(polynom2)

with open('task3_4.txt', 'w') as data:
    data.write(polynom2)
