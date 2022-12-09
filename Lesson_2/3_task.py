# 3) Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

while True:
    try:
        month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
        if month > 12:
            raise Exception()
        break
    except (ValueError, Exception):
        print("Читай внимательнее!!!")

seasons_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
seasons_dict = {0: 'зима', 1: 'зима', 2: 'весна', 3: 'весна', 4: 'весна', 5: 'лето', 6: 'лето', 7: 'лето', 8: 'осень', 9: 'осень', 10: 'осень', 11: 'зима'}

print(seasons_dict.get(seasons_list.index(month)))