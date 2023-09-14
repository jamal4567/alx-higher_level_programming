#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and roman_digits[roman_string[i]] < roman_digits[roman_string[i + 1]]:
            result -= roman_digits[roman_string[i]]
        else:
            result += roman_digits[roman_string[i]]
    return result
