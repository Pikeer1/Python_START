"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
Решение должно работать при любом натуральном N.

Ввод: значение типа <int>
Вывод: значение типа <int>
"""

from random import randint

num = int(input("Введите натуральное число: "))
new_list = [randint(-num, num) for i in range(num)]
print(new_list)

result = 1
with open('indexes.txt', 'r') as file:
    for line in file:
        index = int(line)
        if num > index >= -num:
            result *= new_list[index]
print(result)
