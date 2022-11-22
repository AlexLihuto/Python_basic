# 1 task

try:
    e = "Вы ввели число больше 10!"
    name = input("Введите ваше имя: ")
    surname = input("Введите вашу фамилию: ")
    num = int(input("Введите число от 1 до 10: "))
except ValueError as er:
    print(er)
else:
    if (num > 0 and num < 5):
        print("My name is", name)
    elif (num > 5 and num <= 10):
        print("My surname", surname)
    else:
        print(e)