# 3) Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    return (a + b + c) - min(a, b, c)


while True:
    try:
        a = int(input('Введите 1-ое число: '))
        b = int(input('Введите 2-ое число: '))
        c = int(input('Введите 2-ое число: '))
        break
    except ValueError:
        print('Протри очки и прочитай внимательно!')

print(my_func(a, b, c))

