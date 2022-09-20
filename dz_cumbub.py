# def condition_income():
#     RATE = 6
#     total_income = 0
#     income = int(input('Введите ваш доход\n---> '))
#     total_income += income
#     condition_result = (total_income * RATE) % 100
#     return condition_result
#
#
# def condition_income_minus_expenses():
#     RATE = 15
#     total_expenses = 0
#     income = condition_income()
#     expenses = int(input('Введите ваш расход\n---> '))
#     total_expenses += expenses
#     condition_result = ((income - total_expenses) * RATE) % 100
#     return condition_result
#
#
# def benefit():
#     condition_one = condition_income()
#     condition_two = condition_income_minus_expenses()
#
#     if condition_one > condition_two:
#         difference = condition_one - condition_two
#         print('Мы советуем Вам "УСН Доходы"\n'
#               f'Ваша ставка составит: {condition_one}\n'
#               f'Ставка по второй системе: {condition_two}\n'
#               f'Экономия: {difference}')
#
#     if condition_two > condition_one:
#         difference = condition_two - condition_one
#         print('Мы советуем Вам "УСН Доходы"\n'
#               f'Ваша ставка составит: {condition_two}\n'
#               f'Ставка по второй системе: {condition_one}\n'
#               f'Экономия: {difference}')
# def title():
#     menu = int(input('Выедите номер операции\n'
#                      '1.Добавить доход\n'
#                      '2.Добавить расход\n'
#                      '3.Выбрать систему налогооблажения\n'
#                      'Для выхода введите end\n--> '))
#     return menu
#
#
# if __name__ == '__main__':
#     i = title
#
#     if i == 1:
#         condition_income()
#     if i == 2:
#         condition_income_minus_expenses()
#     if i == 3:
#         benefit()
#     # if title == 'end':
#     #     print("конец")
d = [{"catagory": "Рулевое", "mark": "Рулевая рейка", "model": "Mazda", "pokolenie": "2", "name": 'null', "url": "https://www.autocompas.ru/catalog/rulevaya-reyka/mazda/2-de-3-hetchbek/"},
{"catagory": "Рулевое", "mark": "Рулевая рейка", "model": "Land Rover", "pokolenie": "Freelander", "name": "Рулевая рейка GENERAL RICAMBI 2488333 rv9021 T8C3 3V", "url": "https://www.autocompas.ru/detail/rv9021he-2488333/"},
{"catagory": "Рулевое", "mark": "Рулевая рейка", "model": "Mazda", "pokolenie": "2", "name": '', "url": "https://www.autocompas.ru/catalog/rulevaya-reyka/mazda/2-dj-4-hetchbek/"},
{"catagory": "Рулевое", "mark": "Рулевая рейка", "model": "Lexus", "pokolenie": "IS", "name": "Рулевая рейка LAUBER EB00 6 3410773 5901321062546 665912", "url": "https://www.autocompas.ru/detail/665912v7-3410773/"},
{"catagory": "Рулевое", "mark": "Рулевая рейка", "model": "Land Rover", "pokolenie": "Discovery", "name": 'null', "url": "https://www.autocompas.ru/catalog/rulevaya-reyka/land-rover/discovery-5-l462-vnedorozhnik/"},
{"catagory": "Рулевое", "mark": "Рулевая рейка", "model": "Lexus", "pokolenie": "IS", "name": 'ull', "url": "https://www.autocompas.ru/catalog/rulevaya-reyka/lexus/is-xe20-2-kabriolet/"},
{"catagory": "Рулевое", "mark": "Рулевая рейка", "model": "Lexus", "pokolenie": "RX", "name": "Рулевая рейка LIZARTE 2365122 01512500 8435078364457 X9XI T", "url": "https://www.autocompas.ru/detail/01512500al9-2365122/"},
{"catagory": "Рулевое", "mark": "Рулевая рейка", "model": "Lexus", "pokolenie": "RX", "name": 'null', "url": "https://www.autocompas.ru/catalog/rulevaya-reyka/lexus/rx-al20-4-vnedorozhnik/"},
{"catagory": "Рулевое", "mark": "Рулевая рейка", "model": "Hyundai", "pokolenie": "Verna", "name": 'null', "url": "https://www.autocompas.ru/catalog/rulevaya-reyka/hyundai/verna-hc-4-sedan/"},
{"catagory": "Рулевое", "mark": "Рулевая рейка", "model": "Hummer", "pokolenie": "H3", "name": "Рулевая рейка SERCORE 131041 2EKS9 HC 1JV 2948208", "url": "https://www.autocompas.ru/detail/131041if-2948208/"},
{"catagory": "Рулевое", "mark": "Рулевая рейка", "model": "Hummer", "pokolenie": "H2", "name": 'null', "url": "https://www.autocompas.ru/catalog/rulevaya-reyka/hummer/h2-gmt820-1-vnedorozhnik-5d/"},
{"catagory": "Рулевое", "mark": "Рулевая рейка", "model": "Hummer", "pokolenie": "H2", "name": "Рулевая рейка LIZARTE 8435078359415 R73W8 3 2365701 03341000", "url": "https://www.autocompas.ru/detail/0334100026m-2365701/"},
{"catagory": "Рулевое", "mark": "Рулевая рейка", "model": "Hummer", "pokolenie": "H2", "name": 'null', "url": "https://www.autocompas.ru/catalog/rulevaya-reyka/hummer/h2-gmt820-1-pikap-4d/"},
{"catagory": "Рулевое", "mark": "Рулевая рейка", "model": "Hummer", "pokolenie": "H3", "name": 'null', "url": "https://www.autocompas.ru/catalog/rulevaya-reyka/hummer/h3-gmt345-1-pikap/"}]
data = {'category': 'Рулевая рейка', 'model': 'Lexus'}
for i in d:
    if (data['category'] in i['mark']) and (data['model'] in i['model']):
        print(i['name'])
    else:
        print(['хуй'])