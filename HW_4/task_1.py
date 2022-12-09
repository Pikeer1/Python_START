"""
Выведите список простых множителей натурального числа N.

Ввод: значение типа <int>
Вывод: значение типа <list>

Примеры:
20
[2, 2, 5]

38
[2, 19]
"""

number = int(input("Введите число: "))
divisor = 2
my_list = []
temp_num = number
while divisor <= number:
    if number % divisor == 0:
        my_list.append(divisor)
        number /= divisor
    else:
        divisor += 1
print(f"Простые множители числа {temp_num} = {my_list}")
