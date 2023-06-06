#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lista2 = []
    for x in my_list:
        if x % 2 == 0:
            lista2.append(True)
        else:
            lista2.append(False)
    return lista2
