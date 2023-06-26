#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    new_list = []  # create new list
    quo = None  # declare variable for output

    for i in range(list_length):
        if quo == TypeError or ZeroDivisionError or IndexError:
            quo = 0  # assign 0 to quo when above errors are encountered
        try:
            quo = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(quo)
    return (new_list)
