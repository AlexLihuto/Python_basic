# 5) Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если
# в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
# значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rate_list = [5, 4, 3, 2, 1]
print(f"Рейтинг - {rate_list}")
while True:
    try:
        digit = int(input("Введите число (000 - выход) "))
        while digit != 000:
            rate_list = [5, 4, 3, 2, 1]
            for el in range(len(rate_list)):
                if rate_list[el] == digit:
                    rate_list.insert(el + 1, digit)
                    break
                elif rate_list[0] < digit:
                    rate_list.insert(0, digit)
                elif rate_list[-1] > digit:
                    rate_list.append(digit)
                elif (rate_list[el] > digit and rate_list[el + 1] < digit):
                    rate_list.insert(el + 1, digit)
            print(f"текущий список - {rate_list}")
            digit = int(input("Введите число (000 - выход) "))
        break
    except ValueError:
        print("Читай внимательнее!!!")