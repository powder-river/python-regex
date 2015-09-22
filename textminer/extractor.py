import re

def phone_numbers(s):
    nums = re.findall(r'\(\d{3}\) \d{3}-\d{4}', s)
    return nums
