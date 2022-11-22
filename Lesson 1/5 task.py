# 5 task
try:
    income = int(input("Введите значение выручки: "))
    outcome = int(input("Введите значение издержек: "))
    profit = income - outcome
except ValueError as er:
    print(er)
else:
    if profit < 0:
        print("Фирма отработала в убыток")
    elif profit == 0:
        print("Фирма отработала в ноль, но без убытков")
    else:
        rent = profit / income
        quantity = int(input("Введите численность сотрудников в компании: "))
        profit_quantity = profit / quantity
        print("Фирма отработала с прибылью:", profit, "\nРентабельность выручки:", rent,
              "\nПрибыль фирмы в расчете на одного сотрудника:", profit_quantity)
