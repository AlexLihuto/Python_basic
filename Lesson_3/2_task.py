# 2) Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Реализовать вывод данных о
# пользователе одной строкой.

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year_of_birth = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email: ')
phone_number = input('Введите номер телефона: ')


def user_params(name, surname, year_of_birth, city, email, phone_number):
    return ' '.join([name, surname, year_of_birth, city, email, phone_number])


print(user_params(name, surname, year_of_birth, city, email, phone_number))

