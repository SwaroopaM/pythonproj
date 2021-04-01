# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def palindrome():
    num = int(input("Enter a number: "))
    temp = num
    reverse = 0
    while (num > 0):
        digits = num % 10
        reverse = reverse * 10 + digits
        num = num // 10
    if (temp == reverse):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    palindrome()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
