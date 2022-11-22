# 1 task

name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
while True:
    try:
        num = int(input("Введите число от 1 до 10: "))
        if num > 10:
            raise Exception("Вы ввели число больше 10!")
        break
    except (ValueError, Exception) as er:
        print(er)

if (num > 0 and num < 5):
    print("My name is", name)
else:
    print("My surname", surname)
