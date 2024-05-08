#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    except Exception as e:
        print("An error occured:", e)
        return None
    else:
        return result
    finally:
        print("Inside result: {}".format(result))
