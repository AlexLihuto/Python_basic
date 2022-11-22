# 4 task
try:
    num = int(input("Введите целое положительное число: "))

    max_digit = 0
except ValueError as er:
    print(er)
else:
    while num > 0:
        digit = num % 10
        if digit > max_digit:
            max_digit = digit
            if max_digit == 9:
                break
        num //= 10
    print(max_digit)



