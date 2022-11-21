# print('Hello, world')

# 1 task
# e = "error!!!"
# name = input("Введите ваше имя: ")
# surname = input("Введите вашу фамилию: ")
# num = int(input("Введите число от 1 до 10: "))
#
# if (num > 0 and num < 5) :
#     print("My name is", name)
# elif(num > 5 and num <= 10) :
#     print("My surname", surname)
# else:
#     print(e)

# 2 task
# seconds = int(input("Введите время в секундах: "))
#
# minute = seconds//60
# seconds %= 60
# hour = minute//60
# minute %= 60
#
# if hour > 24:
#     print("Вы ввели слишком большое число!")
# else:
#     print(hour, ":", minute, ":", seconds)

# 3 task
# n = int(input("Введите число от 1 до 9: "))
#
# if n == 0:
#     result = 0
# elif n > 9:
#     result = "Вы ввели число больше 9"
# else:
#     n_n = n * 10 + n
#     n_n_n = n_n * 10 + n
#     result = n + n_n + n_n_n
#
# print(result)

# 4 task
# num = int(input("Введите целое положительное число: "))
#
# max_digit = 0
#
# while num > 0:
#     digit = num % 10
#     if digit > max_digit:
#         max_digit = digit
#         if max_digit == 9:
#             break
#     num //= 10
#
# print(max_digit)

# 5 task
# income = int(input("Введите значение выручки: "))
# outcome = int(input("Введите значение издержек: "))
# profit = income - outcome
#
# if profit < 0:
#     print("Фирма отработала в убыток")
# elif profit == 0:
#     print("Фирма отработала в ноль, но без убытков")
# else:
#     rent = profit/income
#     quantity = int(input("Введите численность сотрудников в компании: "))
#     profit_quantity = profit/quantity
#     print("Фирма отработала с прибылью:", profit, "\nРентабельность выручки:", rent, "\nПрибыль фирмы в расчете на одного сотрудника:", profit_quantity)


# 6 task
a = int(input("Введите растояние пробежки в первый день: "))
b = int(input("Введите растояние-цель: "))

i = 1

while a < b:
    print(f"{i} день: {a}")
    a *= 1.1
    i += 1

print(f"На {i} день спортсмен достиг результата не менее {round(a)} км")

