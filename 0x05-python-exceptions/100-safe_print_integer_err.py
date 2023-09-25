#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        import sys
        sys.stderr.write("Exception: Unknown format code 'd' for object of type 'str'\n")
        return False
