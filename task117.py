from time import *

def chess():
   start = time()
   while time() - start < 1800:
       move = input('Введите ход: ')
       if move.lower() == 'off':
           break
       else:
           print(f'Вы потратили на ход: {round(time() - start, 2)} секунд')
       print(f'Оставшееся время: {30 -  round((time() - start) / 60, 2)} минут')


chess()