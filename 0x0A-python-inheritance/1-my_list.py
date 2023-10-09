#!/usr/bin/python3
''' defines class MyList '''


class MyList(list):
    '''Represent my list '''

    def print_sorted(self):
        '''  prints the list, but sorted '''
        print(sorted(self))
