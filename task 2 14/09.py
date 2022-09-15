print('Welcome, dude!')
start_game = input()
counter = 0
if start_game.lower() == 'game':
    while counter < 3 :
        print('Guess num?')
        num = int(input())
        if num == 5:
            print('You won')
            break
        else:
            print('Try another')
            counter += 1
    print('Game over')
else:
    print('Nope')
