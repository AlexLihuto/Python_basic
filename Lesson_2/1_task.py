#1) Cоздать список и заполнить его элементами различных типов данных. Реализовать скрипт
#проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
#Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = []

my_list.append(False)
my_list.extend(['text', 0.7, 297, None])
my_list.append(False)
my_list.insert(3, None)

print("Список = " + str(my_list) + "\nТипы элементов списка:")

for ind, el in enumerate(my_list):
    print(ind, type(el))