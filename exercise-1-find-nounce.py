'''
Exercise 1: Finding the nounce.
Author: Michelle Xie
'''

import hashlib, string

def build_nounce(start_list, alphanumeric):
    output_list = []
    if len(start_list) == 0:
        return list(alphanumeric)
    for i in start_list:
        for alpha in alphanumeric:
            output_list.append(i+alpha)
    return output_list

def try_hash(input_string, nounce):
    text = input_string + nounce
    hash_result = hashlib.sha256(str.encode(text)).hexdigest()
    if hash_result[0:4] == '0000':
        print("nounce found:", nounce)
        return True
    print("false:", nounce)
    return False
            

def find_nounce(input_string, alphanumeric):
    nounce_list = build_nounce([], alphanumeric)
    while len(nounce_list) > 0:
        nounce = nounce_list.pop(0)
        if try_hash(input_string, nounce):
            return nounce
        else:
            nounce_list += build_nounce([nounce], alphanumeric)


def main():
    alphanumeric = string.ascii_letters + string.digits
    find_nounce('3', alphanumeric)

main()
