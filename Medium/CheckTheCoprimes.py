import math


def checkthecoprimes(liczba):
    ogranicznik = liczba // 2
    for i in range(ogranicznik, 1, -1):
        if math.gcd(liczba, i) == 1:
            return (i)
    return (1)


def main():
    N = int(input())
    for i in range(N):
        liczba = int(input())
        print(checkthecoprimes(liczba))


if __name__ == '__main__':
    main()
