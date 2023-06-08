#!/usr/bin/python3
def uniq_add(my_list=[]):
    lista2 = []
    lista2 = my_list[0:1]
    for i in range(len(my_list)):
        if my_list[i] not in lista2:
            lista2.append(my_list[i])
    suma = sum(lista2)
    return suma
