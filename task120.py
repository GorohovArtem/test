from random import *
def competitions():
    team1 = 0
    team2 = 0
    while True:
        user = input("Для продолжения напишите 'Да', а для завершения 'off': ")
        if user != 'off':
            number = randint(1, 2)
            print('Ваш номер:', number)
            if number == 1:
                team1 += 1
            else:
                team2 += 1
            print('Участников в первом забеге:', team1)
            print('Участников во втором забеге:', team2)
        else:
            break

competitions()