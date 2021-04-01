# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def countLetters():
     value= input("Enter a String: ")
     totalDigits = 0
     totalLetters = 0
     for c in value:
        if c.isdigit():
            totalDigits=totalDigits+1
        else:
            totalLetters=totalLetters+1

     print("Total letters found :-", totalLetters)
     print("Total digits found :-", totalDigits)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    countLetters()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
