def Solution(l):
    for el in l:
        try:
            print(el / 3)
        except TypeError as e:
            print('Невозможно разделить')