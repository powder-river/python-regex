import re

def binary(s):
    num = re.match(r'^[0-1]',s)
    if num == None:
        return False
    else:
        return True


def binary_even(s):
    one_count = 0
    zero_count = 0
    for n in s:
        if n == '1':
            one_count +=1
        elif n == '0':
            zero_count += 1
        else:
            return "ERROR ERROR ERROR"
    if one_count == zero_count:
        return True
    else:
        return False
