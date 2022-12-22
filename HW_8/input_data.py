from write_data import count_data


def input_data():
    dct = dict()
    id = count_data("name.csv")
    dct["id"] = id
    dct["surname"] = input('Введите фамилию: ')
    dct["name"] = input('Введите имя: ')
    dct["class"] = input('Введите класс: ')
    dct["status"] = input('Введите статус: ')
    dct["row"] = input('Введите ряд: ')
    dct["col"] = input('Введите номер парты: ')
    dct["city"] = input('Введите город: ')
    dct["street"] = input('Введите улицу: ')
    dct["house"] = input('Введите дом: ')
    dct["apartament"] = input('Введите номер квартиры: ')
    dct["other"] = input('Введите примечание: ')
    return dct
