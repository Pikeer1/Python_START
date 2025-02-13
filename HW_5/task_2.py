"""
Реализуйте код игры.
Правила игры: на столе лежит N количество конфет. Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой, то есть случаен. За один ход можно забрать не более чем k конфет.
Не брать конфеты НЕЛЬЗЯ. Побеждает тот, кто сделал последний ход, то есть забрал со стола остатки конфет.
Он забирает также все конфеты оппонента.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего оппонента?

a) Добавьте игру против бота
b) Подумайте, как наделить бота простейшим "интеллектом"
"""

from random import randint


def input_name(name):
    x = int(input(f"{name}, введите количество (k) конфет, которое возьмете: "))
    return x


def show_stat(name, k, counter, val):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {val} конфет.")


player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 2)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0
k = 0

while value > k:
    if flag:
        k = input_name(player1)
        counter1 += k
        value -= k
        flag = False
        show_stat(player1, k, counter1, value)

    else:
        k = input_name(player2)
        counter2 += k
        value -= k
        flag = True
        show_stat(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
