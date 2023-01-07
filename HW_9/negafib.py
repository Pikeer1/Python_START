def negafibon(num):
    if num.isdigit():
        number = int(num)
        my_list = [0 for _ in range(number * 2 + 1)]
        my_list[number + 1] = my_list[number - 1] = 1
        for i in range(number - 1):
            my_list[number + 2 + i] = my_list[number + 1 + i] + my_list[number + i]
            my_list[number - 2 - i] = my_list[number + 2 + i] * ((-1) ** (i + 1))
        my_list = [str(n) for n in my_list]
        return ", ".join(my_list)
    else:
        return "Ошибка"
