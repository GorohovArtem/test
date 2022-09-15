meal = input('Прием пищи:').lower()
if meal == 'завтрак':
    print('Каша')
else:
    wish = input('А что именно надо?').lower()
    if wish == 'плотно поесть':
        print('Плов')
    else:
        print('Котлета с пюре')