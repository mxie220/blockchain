'''
Exercise 1: Finding the nounce.
Author: Michelle Xie
'''

import hashlib, string, datetime

def build_nounce(start_list, alphanumeric, nounce_length):
    output_list = []

    if len(start_list) == 0:
        for character in alphanumeric:
            output_list.append(character*nounce_length)
        return output_list

    for nounce in start_list:
        character_index = 0
        while character_index < len(nounce):
            for alpha in alphanumeric:
                if not (nounce[character_index] == alpha):
                    new_nounce = nounce[0:character_index] + alpha + nounce[character_index+1:]
                    output_list.append(new_nounce)
            character_index += 1
    return output_list

def try_hash(input_string, nounce):
    text = input_string + nounce
    hash_result = hashlib.sha256(str.encode(text)).hexdigest()
    if hash_result[0:4] == '0000':
        print("Nounce found: {0}".format(nounce))
        return True
    print("False: {0}, search continues.".format(nounce))
    return False
            
def find_nounce(input_string, alphanumeric, length):
    nounce_length = length - len(input_string)
    nounce_list = build_nounce([], alphanumeric, nounce_length)
    while len(nounce_list) > 0:
        nounce = nounce_list.pop(0)
        if try_hash(input_string, nounce):
            return nounce
        else:
            nounce_list += build_nounce([nounce], alphanumeric, nounce_length)


def main():
    alphanumeric = string.ascii_letters + string.digits
    print("Please enter input:\t")
    user_input = input()
    print("Please input length:")
    try: 
        length = int(input())
    except TypeError:
        print("That's not a number. Please input a number. Thanks!")
    start_time = datetime.datetime.today()
    find_nounce(user_input, alphanumeric, length)
    end_time = datetime.datetime.today()
    print("Time taken: {0}".format(str(end_time-start_time)))

main()
