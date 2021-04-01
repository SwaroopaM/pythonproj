# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import math
from math import radians, sin, cos, acos

def distance(lat1, lon1, lat2, lon2):
     p = 0.017453292519943295
     c = math.cos
     a = 0.5 - c((lat2 - lat1) * p)/2 + c(lat1 * p) * c(lat2 * p) * (1 - c((lon2 - lon1) * p))/2
     d =12742 * math.asin(math.sqrt(a))
     print(d)


if __name__ == '__main__':
    lat1 = 52.2296756
    lon1 = 21.0122287
    lat2 = 52.406374
    lon2 = 16.9251681
    distance(lat1,lon1,lat2,lon2)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
