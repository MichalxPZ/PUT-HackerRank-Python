import math


def sumofgcds(line):
    wynik = 0
    for i in range(1, line[0] + 1):
        for j in range(i, line[0] + 1):
            if i != j:
                wynik = wynik + math.gcd(line[i], line[j])
    print(wynik)


def main():
    N = int(input())
    for i in range(N):
        line = list(map(int, input().split()))
        sumofgcds(line)


if __name__ == '__main__':
    main()