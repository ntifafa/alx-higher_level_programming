#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for i, val in enumerate(my_list):
        if val == search:
            my_list[i] = replace
    return my_list
