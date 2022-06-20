#!/usr/bin/python3import sys
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as ex:
        sys.stderr.write("Exception: ")
        sys.stderr.write(ex.args[0])
        sys.stderr.write("\n")
        return None
