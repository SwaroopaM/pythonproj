# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def listing():
    list = []
    for value in range(1000,3000):
        s = str(value)
        if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
            list.append(s)
    print(",".join(list))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    listing()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
