# 6 task
try:
    a = int(input("Введите растояние пробежки в первый день: "))
    b = int(input("Введите растояние-цель: "))
    i = 1
    print(f"{i} день: {a}")
except ValueError as er:
    print(er)
else:
    while a < b:
        a *= 1.1
        i += 1
        print(f"{i} день: {a}")

    print(f"На {i} день спортсмен достиг результата не менее {round(a)} км")



