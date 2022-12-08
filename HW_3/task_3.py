"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""

import random

number = int(input("Задайте размерность списка: "))
my_list = [round(random.uniform(1, 5), 2) for i in range(number)]
list_2 = []
for i in range(len(my_list)):
    list_2.append(my_list[i] - int(my_list[i]))
result = max(list_2) - min(list_2)
print(f"Сгенерированный список: {my_list}")
print(f"Результат: {round(result, 2)}")
