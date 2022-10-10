"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""
def printparams(par1,par2,par3):
    if par1 != 'None' and par2 != 'None' and par3 != 'None':
        print(par1, par2, par3)
printparams(5,100,50)