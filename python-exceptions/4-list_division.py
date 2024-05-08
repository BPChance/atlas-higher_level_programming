#!/usr/bin/python3
def last_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                if i >= len(my_list_1) or i >= len(my_list_2):
                    raise IndexError("out of range")
                result = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            except (TypeError, ValueError):
                print("wrong type")
                result = 0
            except IndexError:
                print("out of range")
                result = 0
            finally:
                result_list.append(result)
    finally:
        return result_list
