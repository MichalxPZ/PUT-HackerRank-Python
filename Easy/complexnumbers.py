from math import sqrt
from math import atan
from math import pi

def complex(a, b):
    mod = sqrt(a*a + b*b)
    arg = 0
    if a > 0:
        arg = atan(b/a)
    elif a<0 and b>=0:
        arg = atan(b/a) + pi
    elif a<0 and b<0:
        arg = atan(b/a) - pi
    elif a==0 and b>0:
        arg = pi/2
    elif a==0 and b<0:
        arg = -pi/2
    print(mod)
    print(arg)



def main():
    line = input().split(' + ')
    a = int(line[0])
    b = line[1]
    b = b.replace('j', '')
    b = int(b)
    complex(a,b)


if __name__ == '__main__':
    main()

