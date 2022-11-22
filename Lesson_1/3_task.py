# 3 task
while True:
    try:
        n = int(input("Введите число от 1 до 9: "))
        break
    except ValueError as er:
        print(er)

if n == 0:
    result = 0
elif n > 9:
    result = "Вы ввели число больше 9"
else:
    n_n = n * 10 + n
    n_n_n = n_n * 10 + n
    result = int(n) + int(n_n) + int(n_n_n)

print(result)


