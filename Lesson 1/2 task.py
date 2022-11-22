# 2 task
try:
    seconds = int(input("Введите время в секундах: "))

    minute = seconds // 60
    seconds %= 60
    hour = minute // 60
    minute %= 60
except ValueError as er:
    print(er)
else:
    if hour > 24:
        print("Вы ввели слишком большое число!")
    else:
        print(hour, ":", minute, ":", seconds)



