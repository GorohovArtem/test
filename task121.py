from time import *

delete = int(input("Удалить с поля? (если 'Да', введите 1, если 'Нет', введите 2)"))
if delete == 1:
    removed = int(input('На сколько минут?'))
    if (removed == 2) or (removed == 10):
        print('Вы удалены с поля на',removed,'минут(-ы)')
        sleep(removed)
        print('Возвращайтесь на поле')
else:
    pass