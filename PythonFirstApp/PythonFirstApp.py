
import sys
from math import sin,cos, radians


def make_dot_string(x):
    rad = radians(x)
    numspaces = int(20*cos(radians(x))+20)
    st = ' ' * numspaces + 'o'
    return st

def main():
    for i in range(0,1000,12):
        st = make_dot_string(i)
        print(st)



print("Hello, from first python app written with Visual Studio")

for i in range(360):
    print(cos(radians(i)))

main()


