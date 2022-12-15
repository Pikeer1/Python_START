"""
Задайте список случайных чисел. Выведите:
а) список чисел, которые не повторяются в заданном списке,
б) список повторяемых чисел,
в) список без повторений

Ввод: значение типа <list>
Вывод: три объекта типа <list>

Пример:
[1, 2, 3, 5, 1, 5, 3, 10]
[2, 10]
[1, 3, 5]
[1, 2, 5, 3, 10]
"""

from random import randint

lst = [randint(1, 10) for i in range(6)]
lst_1 = []
lst_2 = []
for num in lst:
    if lst.count(num) == 1:
        lst_1.append(num)
    else:
        if lst_2.count(num) == 0:
            lst_2.append(num)

lst_3 = list(set(lst))

print(f"Исходный список: {lst}")
print(f"Неповторяющиеся числа: {lst_1}")
print(f"Повторяющиеся числа: {lst_2}")
print(f"Список без повторений: {lst_3}")
