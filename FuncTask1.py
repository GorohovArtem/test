"""
Напишите программу печатающую бейджики учеников.
Программа запрашивает ввод числа учеников и печатает каждому бейджик. Бейдж содержит название учебного заведения:
«Колледж Сириус», поле для имени:
«Имя: ____» и поле для школы:
«Группа: ____». Напиши программу, печатающую бейджики студентов как на картинке. В завершении программа должна печатать:
«Готово! Заберите бейджики.»
Функция должна принимать имя и группу ученика.
"""
def print_label(number):
    for i in range(0, number):
        name = input('Введите имя')
        group = input('Введите номер группы')
        print('Колледж Сириус')
        print('Имя: ', name)
        print('Группа: ', group)
    print()
    print('Готово! Заберите бейджики.')


_number = int(input('Введите количество студентов'))
print_label(_number