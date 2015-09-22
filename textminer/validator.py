import re

def binary(s):
    num = re.match(r'^[0-1]',s)
    if num == None:
        return False
    else:
        return True
