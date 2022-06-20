#!/usr/bin/python3
def safe_print_division(a, b):
    nb_print = ""
    try:
        nb_print = (a / b)
        return nb_print
    except:
        nb_print = None
        return None
    finally:
        print("Inside result: {}".format(nb_print))
    print("")
    return nb_print
