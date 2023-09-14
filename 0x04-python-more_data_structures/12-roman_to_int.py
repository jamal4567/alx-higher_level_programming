#!usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    Roman_digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in roman_string:
        digits = Roman_digits[i]
        if result < digits * 5:
            result += digits
        else:
            -digits
    return result
