"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def imt_check(_bmi):
    if _bmi < 18.5:
        return 'Недостаточный вес'
    elif 18.5 <= _bmi <= 25:
        return 'ИМТ в норме'
    elif _bmi > 25:
        return 'Избыточный вес'


def imt_general(weight, height):
    bmi = (weight / (height * height)) * 10000
    print('Ваш ИМТ = ', bmi)
    print(imt_check(bmi))


imt_general(int(input('Enter weight: ')), int(input('Enter height: ')))