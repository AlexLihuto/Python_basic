# 1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.

def division(var_1, var_2):
    return var_1/var_2


while True:
    try:
        var_1 = int(input('Введите 1-ое число: '))
        var_2 = int(input('Введите 2-ое число: '))
        result = division(var_1, var_2)
        break
    except ValueError:
        print('Протри очки и прочитай внимательно!')
    except ZeroDivisionError:
        print('Делить на ноль нельзя! Попробуй еще')

print(result)
