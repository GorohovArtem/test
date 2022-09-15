music1 = input('Введите музыкальные предпочтения:')
counter = 0
while music1 != 'off' and counter < 2:
    print('Предпочтение учтено')
    counter += 1
    music1 = input('Введите музыкальные предпочтения:')
print("Система рекомендаций настроена!")