#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as v:
        import sys
        print("Exception: {}".format(v), file=sys.stderr)
        return False
    except TypeError as t:
        import sys
        print("Exception: {}".format(t), file=sys.stderr)
        return False
