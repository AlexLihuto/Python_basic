# 2 task
while True:
    try:
        seconds = int(input("Введите время в секундах: "))
        minute = seconds // 60
        seconds %= 60
        hour = minute // 60
        minute %= 60
        if hour > 24:
            raise Exception("Вы ввели слишком большое число!")
        break
    except (ValueError, Exception) as er:
        print(er)

print(hour, ":", minute, ":", seconds)



