#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        nb_print = 0
        num = ""
        for j in my_list[0:x]:
            nb_print += 1
            num += str(j)
        print(num)
        return nb_print
    except:
        print("Unknown error occurred")
