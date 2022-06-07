#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    multiples_of_two = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples_of_two.append(True)
        else:
            multiples_of_two.append(False)

    return (multiples_of_two)
