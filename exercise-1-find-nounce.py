'''
Exercise 1: Finding the nounce.
Author: Michelle Xie
'''

import hashlib, string, datetime, pickle, os, bz2
from typing import Type

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
    print("False: {0}. Search continues. Press CTRL + C for options.".format(nounce))
    return False
            
def find_nounce(input_string, alphanumeric, length):
    try:
        nounce_length = length - len(input_string)
        filename = os.getcwd() + '/' + input_string + '.bz2'
        if os.path.exists(filename):
            print("Previous state has been found for this input. Would you like to resume?")
            print("Y = yes")
            print("N = no")
            resume = input()
            if resume == "Y" or resume == "yes" or resume == "Yes" or resume == "YES" or resume == "y":
                input_file = bz2.BZ2File(filename, 'rb')
                nounce_list = pickle.load(input_file)
                input_file.close()
                print(type(nounce_list))
            else:
                nounce_list = build_nounce([], alphanumeric, nounce_length)
            os.remove(filename)
        else:
            nounce_list = build_nounce([], alphanumeric, nounce_length)

        while len(nounce_list) > 0:
            nounce = nounce_list.pop(0)
            if try_hash(input_string, nounce):
                return nounce
            else:
                nounce_list += build_nounce([nounce], alphanumeric, nounce_length)

    except KeyboardInterrupt:
        print("Do you want to save the current state?")
        print("Y = yes")
        print("N = no")
        state = input()
        if state == "Y" or state == "y" or state == "yes" or state == "Yes" or state == "YES":
            output_file = bz2.BZ2File(filename, 'wb')
            pickle.dump(nounce_list, output_file)
            output_file.close()
            print("State saved to {0}".format(filename))

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
