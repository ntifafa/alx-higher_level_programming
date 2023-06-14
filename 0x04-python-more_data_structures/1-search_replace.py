#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for i, val in enumerate(my_list):
        if val == 2:
            my_list[i] = 89
    return my_list
