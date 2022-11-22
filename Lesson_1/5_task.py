# 5 task
while True:
    try:
        income = int(input("Введите значение выручки: "))
        break
    except ValueError as er:
        print(er)
while True:
    try:
        outcome = int(input("Введите значение издержек: "))
        break
    except ValueError as er:
        print(er)
profit = income - outcome

if profit < 0:
    print("Фирма отработала в убыток")
elif profit == 0:
    print("Фирма отработала в ноль, но без убытков")
else:
    rent = profit / income
    while True:
        try:
            quantity = int(input("Введите численность сотрудников в компании: "))
            break
        except ValueError as er:
            print(er)
    profit_quantity = profit / quantity
    print("Фирма отработала с прибылью:", profit, "\nРентабельность выручки:", rent,
              "\nПрибыль фирмы в расчете на одного сотрудника:", profit_quantity)
