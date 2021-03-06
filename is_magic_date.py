# Магические даты
# Магическая дата – это дата, когда день, умноженный на месяц, равен числу образованному последними двумя цифрами года.
# Напишите функцию, is_magic(date) которая принимает в качестве аргумента строковое представление корректой даты
# и возвращает значение True если дата является магической и False в противном случае.

# объявление функции
def is_magic(date):
    d = [int(i) for i in date.split('.')]
    if d[0] * d[1] == d[2] % 100:
        return True
    else:
        return False


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
