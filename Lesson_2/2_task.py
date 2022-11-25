#2) Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
#элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
#сохранить на своем месте. Для заполнения списка элементов необходимо использовать
#функцию input()

while True:
    try:
        count = int(input("Введите количество элементов списка: "))
        break
    except ValueError:
        print("Это не похоже на число...")

input_list = []
i = 0
elem = 0

while i < count:
    a = input(f"Введите {i} элемент списка: ")
    if a == 'None' or a == 'none' or a == '':
        inp = None
        input_list.append(inp)
        i += 1
    elif a.isdigit():
        inp = int(a)
        input_list.append(inp)
        i += 1
    elif a == 'True' or a == 'true':
        inp = True
        input_list.append(inp)
        i += 1
    elif a == 'False' or a == 'false':
        inp = False
        input_list.append(inp)
        i += 1
    else:
        input_list.append(a)
        i += 1

print("Ваш список: \n", input_list)

for el in range(int(len(input_list)/2)):
    input_list[elem], input_list[elem + 1] = input_list[elem + 1], input_list[elem]
    elem += 2

print("Изменённый список: \n", input_list)