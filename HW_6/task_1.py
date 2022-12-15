"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.

Ввод: значение типа <str>
Вывод: значение числового типа данных
"""


def get_exp_form(func: str) -> str:
    exp = func.replace('^', '**')
    exp = exp.replace(' ', '')
    exp = exp.replace('+-', '-')
    exp = exp.replace('-+', '-')
    exp = exp.replace(',', '.')

    return exp


def get_right(symb: str, exp: str):
    index = exp.find(symb)
    right_num = ''
    t = 0
    if symb == '**':
        a = index + 2
    else:
        a = index + 1
    sing = (exp[a])
    if sing == '-':
        right_num = right_num + (exp[i])
        a += 1
    elif sing == '+':
        a += 1
    for i in range(a, len(exp)):
        bb = (exp[i])
        if bb.isdigit() or bb == '.':
            right_num = right_num + bb
            if bb == '.':
                t += 1
        else:
            break
    if t > 0:
        right_num = float(right_num)
    else:
        right_num = int(right_num)
    return right_num


def get_left(symb: str, exp: str):
    index = exp.find(symb)
    left_num = ''
    t = 0
    for i in range(index - 1, -1, -1):
        bb = (exp[i])
        if bb.isdigit() or bb == '.':
            left_num = bb + left_num
            if bb == '.':
                t += 1
        else:
            break
    if t > 0:
        left_num = float(left_num)
    else:
        left_num = int(left_num)
    return left_num


def get_calc(symb: str, left_num, right_num):
    if symb == '**':
        return left_num ** right_num
    elif symb == '*':
        return left_num * right_num
    elif symb == '/':
        return left_num / right_num
    elif symb == '+':
        return left_num + right_num
    elif symb == '-':
        return left_num - right_num


def exp_abb(symb: str, exp: str):
    index = exp.find(symb)
    left_num = get_left(symb, exp)
    right_num = get_right(symb, exp)
    res = get_calc(symb, left_num, right_num)
    left = index - len(str(left_num))
    right = left + len(str(left_num) + symb + str(right_num))
    return exp[:left] + str(res) + exp[right:]


def get_priority(symb_1: str, symb_2: str, exp: str) -> str:
    if symb_1 in exp and symb_2 in exp:
        if exp.find(symb_1) > exp.find(symb_2):
            return symb_2
        elif exp.find(symb_1) < exp.find(symb_2):
            return symb_1
    elif symb_1 in exp:
        return symb_1
    elif symb_2 in exp:
        return symb_2


def get_operate(exp: str):
    while '**' in exp:
        symbol = '**'
        exp = exp_abb(symbol, exp)
    while '*' in exp or '/' in exp:
        symbol = get_priority('*', '/', exp)
        exp = exp_abb(symbol, exp)
    while '+' in exp or '-' in exp:
        if exp.find('-') == 0:
            break
        else:
            symbol = get_priority('+', '-', exp)
            exp = exp_abb(symbol, exp)
    result = float(exp)
    if result % 1 == 0:
        result = int(result)
    return result


func = str(input("Введите выражение: "))
expression = get_exp_form(func)
if expression.count('(') != expression.count(')'):
    print(f'Заданное выражение {func} некорректно! Оно содержит непарные скобки!!!')
else:
    while expression.count('(') != 0 or expression.count(')') != 0:
        right_index = expression.find(')')
        item = expression.find('(')
        while expression.find('(', item) != -1:
            if expression.find('(', item + 1) > right_index or expression.find('(', item + 1) == -1:
                left_index = expression.find('(', item)
                break
            else:
                item = expression.find('(', item + 1)
        expr = expression[left_index + 1: right_index]
        res = get_operate(expr)
        expression = expression[:left_index] + str(res) + expression[right_index + 1:]
        expression = expression.replace('+-', '-')
result = get_operate(expression)
print(f'Результат: {result}')

