"""
Напишите генератор выводящий все числа делящиеся на 11 в диапазоне от 0 до 100
"""
# def divide():
#     # a = [i for i in range(0, 100)]
#     for i in range(100):
#         if i%11 == 0:
#             yield i
#
# obj = divide()
# print(next(obj))
# print(next(obj))
# print(next(obj))
a = (i for i in range(0, 100) if i%11== 0)
for i in a:
    print(i)