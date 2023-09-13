#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def ele_to_replace(element):
        if element != search:
            return element
        else:
            return search
    return list(map(ele_to_replace, my_list))
