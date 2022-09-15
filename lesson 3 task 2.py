a = int(input('К оплате:'))
b = int(input('Текущий час:'))
if b >= 10 and b <= 12:
    a = a/2
    print('Счастливые часы, к оплате:', a)
if b >= 20 and b <= 22:
    a = a/4
    print ('Счастливые часы, к оплате:', a)
else:
    print ('К оплате:', a)