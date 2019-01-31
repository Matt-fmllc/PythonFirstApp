
import sys
from math import sin,cos, radians

import numpy as np
import matplotlib.pyplot as plt

def make_dot_string(x):
    rad = radians(x)
    numspaces = int(20*cos(radians(x))+20)
    st = ' ' * numspaces + 'o'
    return st


def CosPlotWithStrings():
    for i in range(0,1000,12):
        st = make_dot_string(i)
        print(st)

def CosPlotWithGraph():
    x = np.arange(0, radians(1800),radians(12))
    plt.plot(x,np.cos(x),'b')
    plt.show()


def main():
    CosPlotWithStrings()
    CosPlotWithGraph()


print("Hello, from first python app written with Visual Studio")

for i in range(360):
    print(cos(radians(i)))

main()


