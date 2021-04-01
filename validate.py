# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
import base64
def encode(value):
    value =bytes(value, 'utf-8')
    encoded_data = base64.b64encode(value)
    print(encoded_data)
    return encoded_data

def decode(value):

    decoded_data = base64.b64decode(value)
    print(decoded_data)

def validateReferenceId(value):
    regex = '[a-zA-Z0-9@$!%*#?&]{12}'
    match_re = re.compile(regex)
    result = re.search(match_re, value)
    if result:
        if(len(value)==12):
            print("Valid Reference Id")
        else:
            print("Invalid Reference Id")

    else:
        print("Invalid Reference Id")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    value = input("Enter a String: ")
    validateReferenceId(value)
    encoded_data=encode(value)
    decode(encoded_data)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
