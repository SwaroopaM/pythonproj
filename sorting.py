# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def search(a,value,start,end):
     if end>=start:
         mid=int(start+(end-1)/2)
         if a[mid]==value :
             return mid
         elif a[mid]>value:
             return search(a,value,start,mid-1)
         else:
             return search(a,value,mid+1,end)
     else:
         return -1

if __name__ == '__main__':
    a = ['swap', 'seethu', 'babloo', 'kusloo', 'rams', 'sasi']
    a=sorted(a)
    print(a)
    value = input("Enter a value: ")
    result =search(a,value,0,len(a))
    if result != -1:
        print("Element is present at index %d" % result)
    else:
        print("Element is not present in array")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
