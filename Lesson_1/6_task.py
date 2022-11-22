# 6 task
while True:
    try:
        a = int(input("Введите растояние пробежки в первый день: "))
        break
    except ValueError as er:
        print(er)
while True:
    try:
        b = int(input("Введите растояние-цель: "))
        break
    except ValueError as er:
        print(er)
i = 1
print(f"{i} день: {a}")
while a < b:
    a *= 1.1
    i += 1
    print(f"{i} день: {a}")

print(f"На {i} день спортсмен достиг результата не менее {round(a)} км")
