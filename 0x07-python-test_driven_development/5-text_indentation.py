#!/usr/bin/python3
'''
module with function text_indentatio
'''


def text_indentation(text):
    ''' prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text: text to be printed
    Raises:
        TypeError: if a text is not a string
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    counter = 0

    while counter < len(text) and text[counter] == ' ':
        counter += 1

    while counter < len(text):
        print(text[counter], end="")
        if text[counter] == '\n' or text[counter] in '.?:':
            if text[counter] in '.?:':
                print('\n')
            counter += 1
            while counter < len(text) and text[counter] == ' ':
                counter += 1
            continue
        counter += 1
