"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""

def numbe(part1,part2,part3):
    if part1  != 'None' and part2 != 'None' and part3 != 'None':
        print(part1, part2, part3)
numbe(5, 25, 102)

