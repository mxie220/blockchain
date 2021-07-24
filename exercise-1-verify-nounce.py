'''
Exercise 1: Verify the nounce.
Author: Michelle Xie
'''

import hashlib

def verify_nounce(user_input, nounce):
    text = user_input + nounce
    hash_result = hashlib.sha256(str.encode(text)).hexdigest()
    print("Hash: {0}".format(hash_result))


print("Enter input:\t") 
user_input = input()
print("Enter nounce:\t") 
nounce = input()
verify_nounce(user_input, nounce)


# # TO RUN AS CONTINUOUS LOOP 
# while True:
#     print("Verifying the nounce.")
#     print("Enter input:\t") 
#     user_input = input()
#     print("Enter nounce:\t") 
#     nounce = input()
#     verify_nounce(user_input, nounce)
#     print("Press Ctrl + C to exit...")
