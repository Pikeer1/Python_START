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

from random import randrange
from os import path, mkdir, chdir


def create_poly(list_koef):
    i = len(list_koef) - 1
    new_poly = ""
    plus = False
    for num in list_koef:
        if num:
            if plus:
                new_poly += " + "
            else:
                plus = True

            if i > 1:
                new_poly += f"{'' if num == 1 else num}x^{i}"
            elif i == 1:
                new_poly += f"{'' if num == 1 else num}x"
            else:
                new_poly += f"{num}"

        i -= 1
    if not new_poly:
        new_poly += "0 = 0"
    else:
        new_poly += " =0"
    return new_poly


if __name__ == '__main__':
    k = int(input("Введите степень k: "))
    polynom = [randrange(101) for i in range(k + 1)]
    string_poly = create_poly(polynom)
    print(string_poly)

    if not path.isdir("polynom"):
        mkdir("polynom")
    chdir("polynom")
    i = 0
    while True:
        if not path.isfile(f"polynom_{i}.txt"):
            with open(f"polynom_{i}.txt", 'w') as file:
                file.write(string_poly)
                print(f"Результат в файле polynom_{i}.txt")
            break
        else:
            i += 1
