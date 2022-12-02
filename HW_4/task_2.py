"""
Задайте список случайных чисел. Выведите список чисел, которые не повторяются в заданном списке.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
[2, 4, 6, 8]
"""

from random import randint

number = int(input("Задайте размерность списка: "))
first_list = [randint(1, 8) for i in range(number)]
second_list = []
for i in first_list:
    if first_list.count(i) == 1:
        second_list.append(i)
print(f"Исходный список: {first_list}")
print(f"Список из неповторяющихся элементов: {second_list}")
